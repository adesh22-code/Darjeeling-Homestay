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
    path(
    "owner/delete/<int:id>/",
    owner_views.delete_homestay,
    name="delete_homestay",
    ),
    path(
    "owner/bookings/",
    owner_views.owner_bookings,
    name="owner_bookings",
    ),
    path(
    "owner/booking/<int:booking_id>/confirm/",
    owner_views.confirm_booking,
    name="confirm_booking",
    ),

    path(
    "owner/booking/<int:booking_id>/cancel/",
    owner_views.cancel_booking,
    name="cancel_booking",
    ),
    path(
    "booking/<int:booking_id>/cancel/",
    views.cancel_booking,
    name="customer_cancel_booking",
    ),
    path(
    "owner/booking/<int:booking_id>/status/",
    owner_views.update_booking_status,
    name="update_booking_status",
    ),
]
