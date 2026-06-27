from django.db import models

class Homestay(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.IntegerField()
    image = models.ImageField(upload_to="homestays/", blank=True, null=True)
    description = models.TextField(blank=True)

    bedrooms = models.PositiveIntegerField(default=1)

    bathrooms = models.PositiveIntegerField(default=1)

    max_guests = models.PositiveIntegerField(default=2)

    wifi = models.BooleanField(default=True)

    parking = models.BooleanField(default=False)

    breakfast = models.BooleanField(default=False)

    def __str__(self):
        return self.name
