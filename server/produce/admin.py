from django.contrib import admin
from produce.models import Product, Order, Services, OrderServices, ProductItem, OrderServices


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    list_display_links = ('name', 'price', 'status')
    list_filter = ('name', 'price', 'status', 'description')
    search_fields = ('name', 'price', 'status', 'description')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    list_display_links = ('name', 'price', 'status')
    list_filter = ('name', 'price', 'status', 'description')
    search_fields = ('name', 'price', 'status', 'description')


@admin.register(OrderServices)
class OrderServicesAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'status')
    list_display_links = ('user', 'price', 'status')
    list_filter = ('price', 'status',)
    search_fields = ('price', 'status')


class ProductItemInline(admin.TabularInline):
    model = ProductItem
    fields = ('product','quantity',)
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'status', 'phone')
    list_display_links = ('user', 'price', 'status', 'phone')
    list_filter = ('user', 'price', 'status', 'phone')
    search_fields = ('user', 'price', 'status', 'phone')
    inlines = [ProductItemInline]
