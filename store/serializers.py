from rest_framework import serializers

from .models import ProductModel

class ProductModelSerializer(serializers.ModelSerializer):

	class Meta():
		model = ProductModel
		fields = ['name','slug','price','manufacturer','guarantee','info']

