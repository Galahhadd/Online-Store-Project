from django.views.generic import TemplateView
from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .models import ProductModel, CartItemModel, CartModel
from .serializers import ProductModelSerializer, CartItemSerializer, CartSerializer
from .filters import AllWillBeOneFilter

class HomePageView(TemplateView):
	template_name = "home.html"

@api_view(['GET'])
def EndPointsView(request):
	endpoints = {
		"API all products" : {
					"endpoint":"products/",
					"methods":"GET",
					"info":"Return all rpoducs from data base"
						},

		"API search product" : {
					"endpoint":"products/search/?name=",
					"methods":"GET",
					"info":"Returns products with given name",
					"example":"products/search/?name=amd"
						},

		"API single products" : {
					"endpoint":"products/<slug>/",
					"methods":"GET",
					"info":"Returns single product with given slug",
					"example":"products/amd-ryzen-5600"
						},	

		"API register user" : {
					"endpoint":"accounts/register/",
					"methods":"POST",
					"info":"Registers new user",
					"fields":{
							    "email": "",
							    "first_name": "",
							    "last_name": "",
							    "phone_number": "",
							    "password": "",
							    "password2": ""
							}
						},	

		"API login user" : {
					"endpoint":"accounts/login/",
					"methods":"POST",
					"info":"User logins and obtains two tokens, access token need to access API endpoints with permission_classes, refresh needed to create new access token",
					"fields":{
							    "email": "",
							    "password": ""
							},
					"response":{
								"refresh":"<some value>",
								"access": "<some value>"
							}	
						},	

		"API access token refresh" : {
					"endpoint":"accounts/login/refresh/",
					"methods":"POST",
					"info":"Requires refresh token to generate new access token and refresh tokens",
					"fields":{
							    "refresh": ""
							},
					"response":{
								"refresh":"<some value>",
								"access": "<some value>"
							}	
						},	
		"API user profile" : {
					"endpoint":"accounts/profile/",
					"methods":"GET",
					"info":"Shows profile of current logged in user",
					"requires":"access token"
						},
		"API get all products" : {
					"endpoint":"products/",
					"methods":"GET",
					"info":"Shows all products",
						},	
		"API get specific product by slug" : {
					"endpoint":"products/<slug>",
					"methods":"GET",
					"info":"Shows specific product by its slug",
					"example":"/products/intel-core-i7-10700k"
						},	
		"API filter products" : {
					"endpoint":"products/filter/",
					"methods":"GET",
					"info":"Filter prodctucts by given filter values",
					"example":"/products/filter/?manufacturer=AMD",
					"example_2":"/products/filter/?min_price=390&info=type:CPU;core:Zen%203"
						},										
	}
	return Response(endpoints)


class GetProducstApiView(generics.ListAPIView):
	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer

class RetrieveProductApiView(generics.RetrieveAPIView):
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


class FilterProductsApiView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductModelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AllWillBeOneFilter


class CartItemApiView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
	queryset = CartItemModel.objects.all()
	serializer_class = CartItemSerializer
	lookup_field = 'pk'


class CartApiView(generics.ListAPIView):
	serializer_class = CartSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		print(CartModel.objects.filter(customer=self.request.user.customer))
		return CartModel.objects.filter(customer=self.request.user.customer)
  

