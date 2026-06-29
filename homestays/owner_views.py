from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms_owner import HomestayForm

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



@login_required
def add_homestay(request):

    if request.user.user_type != "owner":
        return render(
            request,
            "403.html",
            status=403,
        )

    if request.method == "POST":

        form = HomestayForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            homestay = form.save(commit=False)

            homestay.owner = request.user

            homestay.save()

            return redirect("owner_dashboard")

    else:

        form = HomestayForm()

    return render(
        request,
        "homestays/add_homestay.html",
        {
            "form": form,
        },
    )
