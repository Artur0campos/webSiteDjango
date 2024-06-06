from django.urls import path
from myApp.views import home

urlpatterns = [
    path("", home)
]