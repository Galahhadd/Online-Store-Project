from rest_framework import serializers

from .models import ProductModel

class ProductModelSerializer(serializers.ModelSerializer):

	class Meta():
		model = ProductModel
		fields = ['name','slug','price','manufacturer','guarantee','info']
		lookup_field = 'slug'
		extra_kwargs = {
		    'url': {'lookup_field': 'slug'}
		}



