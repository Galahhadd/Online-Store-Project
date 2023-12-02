from django.contrib import admin

from .models import ProductModel, CartModel, CartItemModel, ShippingAdressModel, Customer

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug','price','manufacturer','guarantee','info']

@admin.register(CartModel)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['customer','date_ordered','complete','transaction_id']

@admin.register(CartItemModel)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['product','customer','quantity','date_added']

@admin.register(ShippingAdressModel)
class ShippingAdressAdmin(admin.ModelAdmin):
	list_display = ['address','city','zipcode','date_added']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['user','address']

