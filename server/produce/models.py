from django.db import models
from user.models import MyUser

# Create your models here.
class Product(models.Model):
    name = models.CharField('название', max_length=255)
    price = models.IntegerField('Цена')
    image = models.ImageField(upload_to='media/product/%Y/%m')
    description = models.TextField('Описание')


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    price = models.IntegerField('Цена', default=0)
    product = models.ManyToManyField(Product, verbose_name='продукты', blank=True, related_name='product')

    def accept_order(self):
        self.status = False
        self.save()
        return self
