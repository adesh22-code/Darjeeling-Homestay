from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPES = (
        ("customer", "Customer"),
        ("owner", "Owner"),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default="customer"
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
