from rest_framework.serializers import ModelSerializer
from produce.models import Product, ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['categories'] = ProductCategorySerializer(instance.categories.all(), many=True).data
        return rep