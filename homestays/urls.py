from django.urls import path
from .views import home
from . import owner_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("homestay/<int:id>/", views.homestay_detail, name="homestay_detail"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path(
    "owner/dashboard/",
    owner_views.owner_dashboard,
    name="owner_dashboard",
    ),
    path(
    "owner/add/",
    owner_views.add_homestay,
    name="add_homestay",
    ),
    path(
    "owner/edit/<int:id>/",
    owner_views.edit_homestay,
    name="edit_homestay",
    ),
]
