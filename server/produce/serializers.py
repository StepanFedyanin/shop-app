from rest_framework.serializers import ModelSerializer
from produce.models import Product, Order, ProductItem


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductItemSerializer(ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('id','product','quantity')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = ProductSerializer(Product.objects.get(id=rep['product'])).data
        return rep


class ProductItemPostSerializer(ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'price')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['products'] = ProductItemSerializer(ProductItem.objects.filter(order=rep['id']), many=True).data
        return rep
