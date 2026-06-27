from django.contrib import admin
from .models import Homestay


@admin.register(Homestay)
class HomestayAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'price_per_night',
        'available_rooms',
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
