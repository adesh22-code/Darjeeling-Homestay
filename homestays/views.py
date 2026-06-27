from .models import Homestay
from django.shortcuts import render, get_object_or_404


def home(request):
    homestays = Homestay.objects.all()

    return render(
        request,
        "homestays/home.html",
        {
            "homestays": homestays
        }
    )
def homestay_detail(request, id):
    homestay = get_object_or_404(Homestay, id=id)

    return render(
        request,
        "homestays/detail.html",
        {
            "homestay": homestay
        }
    )
