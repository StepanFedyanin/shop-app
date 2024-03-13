from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from produce.serializers import ProductSerializer
from produce.models import Product
from produce.schemas import (ProduceListSchema)

# Create your views here.
class ProduceViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    schema = ProduceListSchema()

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        produce = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(produce)
        return Response(serializer.data, status=status.HTTP_200_OK)