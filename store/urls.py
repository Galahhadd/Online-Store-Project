from django.urls import path

from .views import HomePageView, GetProducstApiView, RetrieveProductAPiView, SearchProductsApiView

app_name = 'store'

urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
	path("products/", GetProducstApiView.as_view(), name='get_products'),
	path('products/<slug:slug>', RetrieveProductAPiView.as_view(), name='retrieve_product'),
	path('products/search/name', SearchProductsApiView.as_view(), name='search_product')
]