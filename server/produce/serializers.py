from rest_framework.serializers import ModelSerializer
from produce.models import Product, Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'price')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = ProductSerializer(instance.product.all(), many=True).data
        return rep
