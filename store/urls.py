from django.urls import path

from .views import HomePageView

app_name = 'store'

urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
]