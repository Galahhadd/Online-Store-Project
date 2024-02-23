from django.views.generic import TemplateView
from django.db.models import Q, F


from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework import status

from .models import ProductModel, OrderModel, CommentModel
from .serializers import (ProductModelSerializer, 	
							OrderSerializerAnonim, 
							AdressSerailizer, 
							ShippingAdressModel, 
							OneProductSerializer, 
							CommentCreateUpdateSerializer,
							FavouriteProductSerializer,)

from .filters import AllWillBeOneFilter


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
	}
	return Response(endpoints)


class GetProducstApiView(generics.ListAPIView):

	"""List all products in Data Base"""

	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer

class RetrieveProductApiView(generics.RetrieveAPIView):

	""" Retrieve single product by slug"""

	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = OneProductSerializer
	lookup_field = 'slug'

class SearchProductsApiView(generics.ListAPIView):

	""" Search product by it's symbols in its name"""

	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer


	def get_queryset(self):

		queryset = ProductModel.objects.all()
		name = self.request.query_params.get('name')
		if name is not None:
			queryset = queryset.filter(Q(name__icontains=name))
		return queryset


class FilterProductsApiView(generics.ListAPIView):

	"""
	Filter products by specific condtions

	"""

	queryset = ProductModel.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = ProductModelSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = AllWillBeOneFilter


class AuthOrderApiView(APIView):
	
	pass



class OrderApiView(APIView):

	""" Creates order """

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:

			""" TO DO for logged in User"""
			
			return Response("I am Authenticated")

		else:
			
			serializer = OrderSerializerAnonim(data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetOrderApi(generics.RetrieveAPIView):
	queryset = OrderModel.objects.all()
	serializer_class = OrderSerializerAnonim
	permission_classes = (AllowAny,)
	lookup_field = 'id'

  

class UpdateComment(generics.RetrieveUpdateAPIView):
	queryset = CommentModel.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = CommentCreateUpdateSerializer
	lookup_field = 'id'


class CreateComment(generics.CreateAPIView):
	queryset = CommentModel.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = CommentCreateUpdateSerializer



class FavoriteProductUpd(generics.RetrieveUpdateAPIView):

	""" TO DO - create separate Create and Delete"""

	queryset = ProductModel.objects.all()
	serializer_class = FavouriteProductSerializer
	permission_classes = (IsAuthenticated,)
	lookup_field = 'slug'

	
