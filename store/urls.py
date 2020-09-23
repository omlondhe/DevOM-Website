from django.urls import path
from . import views

urlpatterns = [
    path("", views.storeHome, name="storeHome"),
    path("<str:slug>", views.storeApp, name="storeApp")
]
