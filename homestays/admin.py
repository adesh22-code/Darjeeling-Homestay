from django.contrib import admin
from .models import Homestay, Booking, Review, HomestayImage

@admin.register(HomestayImage)
class HomestayImageAdmin(admin.ModelAdmin):

    list_display = (
        "homestay",
        "caption",
    )

    list_filter = (
        "homestay",
    )

    search_fields = (
        "homestay__name",
        "caption",
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
