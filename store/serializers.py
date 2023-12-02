from rest_framework import serializers

from .models import ProductModel, CartItemModel, CartModel

class ProductModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductModel
		fields = ['name','slug','price','manufacturer','guarantee','info']
		lookup_field = 'slug'
		extra_kwargs = {
		    'url': {'lookup_field': 'slug'}
		}

class CartItemSerializer(serializers.ModelSerializer):
	product = ProductModelSerializer()
	customer = serializers.ReadOnlyField(source='customer.user.email')

	class Meta:
		model = CartItemModel
		fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True)

    class Meta:
        model = CartModel
        fields = ['products']




