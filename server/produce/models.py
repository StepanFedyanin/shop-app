from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('название категории', max_length=255)


# Create your models here.
class Product(models.Model):
    name = models.CharField('название', max_length=255)
    price = models.IntegerField('Цена')
    image = models.ImageField(upload_to='product/%Y/%m')
    description = models.TextField('Описание')
    categories = models.ManyToManyField(ProductCategory, null=True)


# class Order(models.Model):
#     name = models.CharField('название', max_length=255)
#     price = models.IntegerField('Цена')
#     image = models.ImageField(upload_to='media/product/%Y/%m')
#     description = models.TextField('Описание')
#     categories = models.ManyToManyField(ProductCategory, null=True)
