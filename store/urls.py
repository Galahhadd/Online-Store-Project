from django.urls import path

from .views import (
					GetProducstApiView, 
					RetrieveProductApiView, 
					SearchProductsApiView, 
					EndPointsView,
					FilterProductsApiView,
					CartItemApiView,
					CartApiView,
					)

app_name = 'store'

urlpatterns = [
	path("", EndPointsView, name="home"),
	path("products/", GetProducstApiView.as_view(), name='get_products'),
	path('products/<slug:slug>', RetrieveProductApiView.as_view(), name='retrieve_product'),
	path('products/search/', SearchProductsApiView.as_view(), name='search_product'),
	path('products/filter/', FilterProductsApiView.as_view()),
	path('products/cartitem/<int:pk>', CartItemApiView.as_view()),
	path('products/cart/',CartApiView.as_view()),
]