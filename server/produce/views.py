from itertools import product

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from produce.serializers import ProductSerializer, OrderSerializer, ProductItemSerializer, ProductItemPostSerializer, \
    ServicesSerializer, ServicesSerializer, ServicesPostSerializer, ServicesItemSerializer
from produce.models import Product, Order, ProductItem, Services, OrderServices
from produce.schemas import DeleteSchema, PaySchema, ProduceOrderSchema, ServicesAddOrderSchema, PayServicesSchema


def calculationTotalPrice(order, data):
    total_price = 0
    for product in data['products']:
        total_price += product['product']['price'] * product['quantity']
    data['price'] = total_price
    serializer = OrderSerializer(order, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def calculationServicesTotalPrice(services, data):
    total_price = 0
    for item in data['services']:
        total_price += item['price']
    data['price'] = total_price
    serializer = ServicesSerializer(services, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProduceViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(status=True)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = self.request.user
        queryset = Product.objects.all()
        produce = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(produce)
        if user.is_authenticated:
            order = Order.objects.get_or_create(user=user, status=True)[0]
            serializer_order = OrderSerializer(order).data
            quantity = 0
            product_order = None
            for pr in serializer_order['products']:
                if pr['product']['id'] == produce.id:
                    quantity = quantity + pr['quantity']
                    product_order = pr['id']
            data = serializer.data
            data['product_order'] = product_order
            data['quantity'] = quantity
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.data
            data['quantity'] = False
            data['quantity'] = None
            return Response(data, status=status.HTTP_200_OK)


class OrderViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(type='reduction_opened')

    @action(
        detail=False,
        methods=['post'],
        schema=ProduceOrderSchema()
    )
    def add_item(self, request):
        user = self.request.user
        order = Order.objects.get_or_create(user=user, status=True)[0]
        serializerOrder = OrderSerializer(order)
        params = {
            'product': request.data['id'],
            'quantity': request.data['quantity'],
            'order': serializerOrder.data['id']
        }
        serializer = ProductItemPostSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
            return calculationTotalPrice(order, OrderSerializer(order).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=['post'],
        schema=ProduceOrderSchema()
    )
    def change_item(self, request):
        order_item = get_object_or_404(ProductItem, pk=request.data['id'])
        user = self.request.user
        order = Order.objects.get_or_create(user=user, status=True)[0]
        serializer = ProductItemPostSerializer(order_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return calculationTotalPrice(order, OrderSerializer(order).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=['get'],
    )
    def get_list(self, request):
        user = self.request.user
        order = Order.objects.get_or_create(user=user, status=True)[0]
        serializer = OrderSerializer(order)
        return calculationTotalPrice(order, serializer.data)

    @action(
        detail=False,
        methods=['post'],
        schema=DeleteSchema()
    )
    def remove(self, request):
        try:
            user = self.request.user
            productItem = ProductItem.objects.get(pk=request.data['id'])
            productItem.delete()
            order = Order.objects.get(user=user, status=True)
            serializer = OrderSerializer(order)
            return calculationTotalPrice(order, serializer.data)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=['post'],
        schema=DeleteSchema()
    )
    def remove_by_id_product(self, request):
        try:
            user = self.request.user
            order = Order.objects.get(user=user, status=True)
            productItem = ProductItem.objects.get(order=order, product=request.data['id'])
            productItem.delete()
            order = Order.objects.get(user=user, status=True)
            serializer = OrderSerializer(order)
            return calculationTotalPrice(order, serializer.data)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=['post'],
        schema=PaySchema()
    )
    def pay(self, request):
        try:
            user = self.request.user
            order = Order.objects.get(user=user, status=True)
            order.accept_order(request.data['phone'])
            return Response(status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ServicesViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = Services.objects.filter(status=True)
        serializer = ServicesItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = self.request.user
        queryset = Services.objects.get(pk=pk)
        data = ServicesItemSerializer(queryset).data
        already = False
        services_id = None
        if user.is_authenticated:
            services_order = OrderServices.objects.get_or_create(user=user, status=True)[0]
            serializer = ServicesSerializer(services_order).data
            for pr in serializer['services']:
                if pr['id'] == int(pk):
                    already = True
                    services_id = pr['id']
        data['already'] = already
        data['services_order'] = services_id
        return Response(data, status=status.HTTP_200_OK)


class ServicesOrderViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        services_order = OrderServices.objects.get_or_create(user=user, status=True)[0]
        serializer = ServicesSerializer(services_order)
        return calculationServicesTotalPrice(services_order, serializer.data)

    @action(
        detail=False,
        methods=['post'],
        schema=ServicesAddOrderSchema()
    )
    def add(self, request):
        user = self.request.user
        services = get_object_or_404(Services, pk=request.data['id'])
        services_order = OrderServices.objects.get_or_create(user=user, status=True)[0]
        services_order.services.add(services)
        serializer = ServicesSerializer(services_order)
        return calculationServicesTotalPrice(services_order, serializer.data)

    @action(
        detail=False,
        methods=['post'],
        schema=ServicesAddOrderSchema()
    )
    def remove(self, request):
        user = self.request.user
        services = get_object_or_404(Services, pk=request.data['id'])
        services_order = OrderServices.objects.get_or_create(user=user, status=True)[0]
        services_order.services.remove(services)
        serializer = ServicesSerializer(services_order)
        return calculationServicesTotalPrice(services_order, serializer.data)

    @action(
        detail=False,
        methods=['post'],
        schema=PayServicesSchema()
    )
    def pay(self, request):
        try:
            user = self.request.user
            order = OrderServices.objects.get_or_create(user=user, status=True)[0]
            order.accept_order(request.data['time_start'], request.data['time_end'], request.data['date'], request.data['phone'])
            return Response(status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
