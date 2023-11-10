from django.views.generic import TemplateView
from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import filters

from .models import ProductModel
from .serializers import ProductModelSerializer

class HomePageView(TemplateView):
	template_name = "home.html"

class GetProducstApiView(generics.ListAPIView):
	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer

class RetrieveProductAPiView(generics.RetrieveAPIView):
	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer
	lookup_field = 'slug'

class SearchProductsApiView(generics.ListAPIView):
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer

	def get_queryset(self):

		queryset = ProductModel.objects.all()
		name = self.request.query_params.get('name')
		if name is not None:
			queryset = queryset.filter(Q(name__icontains=name))
		return queryset

