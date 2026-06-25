from django.shortcuts import render
from .models import Homestay


def home(request):
    homestays = Homestay.objects.all()

    return render(
        request,
        "homestays/home.html",
        {
            "homestays": homestays
        }
    )
