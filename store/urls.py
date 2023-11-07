from django.urls import path

from .views import HomePageView, ProductApiView

app_name = 'store'

urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
	path("products/", ProductApiView.as_view(), name='products')
]