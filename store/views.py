from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import ProductModel
from .serializers import ProductModelSerializer

class HomePageView(TemplateView):
	template_name = "home.html"

class ProductApiView(generics.ListAPIView):
	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer
