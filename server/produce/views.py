from itertools import product

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from produce.serializers import ProductSerializer, OrderSerializer
from produce.models import Product, Order
from produce.schemas import DeleteSchema, PaySchema

def calculationTotalPrice(order, data):
    total_price = 0
    for dish in data['product']:
        total_price += dish['price']
    data['price'] = total_price
    serializer = OrderSerializer(order, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class ProduceViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
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
            is_available = False
            for pr in serializer_order['product']:
                if pr['id'] == produce.id:
                    is_available = True
            data = serializer.data
            data['available'] = is_available
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.data
            data['available'] = False
            return Response(data, status=status.HTTP_200_OK)


class OrderViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        user = self.request.user
        product = get_object_or_404(Product, pk=pk)
        order = Order.objects.get_or_create(user=user, status=True)[0]
        order.product.add(product)
        serializer = OrderSerializer(order)
        return calculationTotalPrice(order, serializer.data)

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
            order = Order.objects.get(user=user, status=True)
            product = get_object_or_404(Product, pk=request.data['id'])
            order.product.remove(product)
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
            order.accept_order()
            return Response(status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)