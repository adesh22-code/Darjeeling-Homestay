from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CustomerRegistrationForm


def register(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Ensure every registration is a customer
            user.user_type = "customer"
            user.save()

            login(request, user)

            return redirect("home")

    else:
        form = CustomerRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )
