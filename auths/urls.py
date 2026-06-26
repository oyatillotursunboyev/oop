from django.urls import path
from .views import *
urlpatterns = [
    path("register/", register, name="Register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
];
