from django.urls import path

from . import views

urlsPatterns = [
    path("", views.home, name="home")
]