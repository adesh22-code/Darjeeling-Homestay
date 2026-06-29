from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Homestay


@login_required
def owner_dashboard(request):

    if request.user.user_type != "owner":
        return render(
            request,
            "403.html",
            status=403,
        )

    homestays = Homestay.objects.filter(owner=request.user)

    return render(
        request,
        "homestays/owner_dashboard.html",
        {
            "homestays": homestays,
        },
    )
