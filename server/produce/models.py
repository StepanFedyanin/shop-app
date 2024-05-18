from datetime import datetime

from django.db import models
from user.models import MyUser


class Services(models.Model):
    name = models.CharField('Название услуги', max_length=255)
    price = models.IntegerField('Цена')
    image = models.ImageField(upload_to='media/services/%Y/%m')
    description = models.TextField('Описание')
    status = models.BooleanField('Отображать', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Product(models.Model):
    name = models.CharField('название', max_length=255)
    price = models.IntegerField('Цена')
    image = models.ImageField(upload_to='media/product/%Y/%m')
    description = models.TextField('Описание')
    status = models.BooleanField('Отображать', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class OrderServices(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.BooleanField('Статус', default=True)
    price = models.IntegerField('Цена', default=0)
    services = models.ManyToManyField(Services, verbose_name='Услуги', blank=True, related_name='services', null=True)
    date = models.DateField('Дата оказания услуг', null=True)
    time_start = models.TimeField('Удобное время оказания услуг с', null=True)
    time_end = models.TimeField('Удобное время оказания услуг по', null=True)
    phone = models.CharField('Контактный телефон', max_length=20, blank=True, default='')

    def accept_order(self, time_start, time_end, date, phone):
        self.status = False
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.time_start = time_start
        self.time_end = time_end
        self.phone = phone
        self.save()
        return self

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Заказы услуг'
        verbose_name_plural = 'Заказы услуг'


class Order(models.Model):
    user = models.ForeignKey(MyUser,verbose_name='Пользователь', on_delete=models.CASCADE)
    status = models.BooleanField('Статус', default=True)
    price = models.IntegerField('Цена', default=0)
    phone = models.CharField('Контактный телефон', max_length=20, blank=True, default='')
    data = models.DateTimeField('Дата и время оформления заказа', null=True, blank=True)
    def accept_order(self, phone):
        self.status = False
        self.phone = phone
        self.save()
        return self

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class ProductItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукты', blank=True, related_name='product', null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField('Колличество', default=1)
    order = models.ForeignKey(Order, verbose_name='Тендер', null=True, related_name='lots', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
