from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.customer_login, name="login"),
    path("logout/", views.customer_logout, name="logout"),
]
