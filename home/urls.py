from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("donate", views.donate, name="donate"),
    path("donateHandler", views.donateHandler, name="donateHandler"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
    path("signup", views.signUp, name="signUp"),
    path("login", views.userLogin, name="userLogin"),
    path("logout", views.userLogout, name="userLogout"),
    path("<str:slug>", views.errorHandler, name="errorHandler"),
]
