from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("homestay/<int:id>/", views.homestay_detail, name="homestay_detail"),
]
