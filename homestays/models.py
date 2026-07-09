from django.db import models
from django.conf import settings

class Homestay(models.Model):
    
    owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="homestays",
    null=True,
    blank=True,
    )
    
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


class Booking(models.Model):
    STATUS_CHOICES = (
    ("pending", "Pending"),
    ("confirmed", "Confirmed"),
    ("cancelled", "Cancelled"),
    ("completed", "Completed"),
    )
    
    homestay = models.ForeignKey(
        Homestay,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="bookings",
    null=True,
    blank=True,
    )

    guest_name = models.CharField(max_length=100)

    guest_email = models.EmailField()

    guest_phone = models.CharField(max_length=15)

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="pending",
    )

    def __str__(self):
        return f"{self.guest_name} - {self.homestay.name}"



class Review(models.Model):

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="review"
    )

    homestay = models.ForeignKey(
        Homestay,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.homestay.name} ({self.rating}⭐)"
