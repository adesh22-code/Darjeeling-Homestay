from django.contrib import admin
from .models import Homestay, Booking, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "homestay",
        "rating",
        "created_at",
    )

    list_filter = (
        "rating",
        "created_at",
    )

    search_fields = (
        "user__username",
        "homestay__name",
    )


@admin.register(Homestay)
class HomestayAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "price_per_night",
        "available_rooms",
        "bedrooms",
        "bathrooms",
        "max_guests",
    )

    list_filter = (
        "wifi",
        "parking",
        "breakfast",
    )

    search_fields = (
        "name",
        "location",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "guest_name",
        "homestay",
        "check_in",
        "check_out",
        "guests",
        "created_at",
    )

    list_filter = (
        "check_in",
        "check_out",
        "created_at",
    )

    search_fields = (
        "guest_name",
        "guest_email",
        "guest_phone",
    )
