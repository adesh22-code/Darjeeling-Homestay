from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms_owner import HomestayForm
from .models import Homestay, Booking
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required



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


@login_required
def edit_homestay(request, id):

    if request.user.user_type != "owner":
        return render(
            request,
            "403.html",
            status=403,
        )

    homestay = get_object_or_404(
        Homestay,
        id=id,
        owner=request.user,
    )

    if request.method == "POST":

        form = HomestayForm(
            request.POST,
            request.FILES,
            instance=homestay,
        )

        if form.is_valid():
            form.save()
            return redirect("owner_dashboard")

    else:

        form = HomestayForm(instance=homestay)

    return render(
        request,
        "homestays/edit_homestay.html",
        {
            "form": form,
            "homestay": homestay,
        },
    )


@login_required
def delete_homestay(request, id):

    if request.user.user_type != "owner":
        return render(
            request,
            "403.html",
            status=403,
        )

    homestay = get_object_or_404(
        Homestay,
        id=id,
        owner=request.user,
    )

    if request.method == "POST":
        homestay.delete()
        return redirect("owner_dashboard")

    return render(
        request,
        "homestays/delete_homestay.html",
        {
            "homestay": homestay,
        },
    )

@login_required
def owner_bookings(request):

    if request.user.user_type != "owner":
        return render(
            request,
            "403.html",
            status=403,
        )

    bookings = Booking.objects.filter(
        homestay__owner=request.user
    ).select_related(
        "homestay",
        "user",
    ).order_by("-created_at")

    return render(
        request,
        "homestays/owner_bookings.html",
        {
            "bookings": bookings,
        },
    )

@login_required
def confirm_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        homestay__owner=request.user,
    )

    booking.status = "confirmed"
    booking.save()

    return redirect("owner_bookings")


@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        homestay__owner=request.user,
    )

    booking.status = "cancelled"
    booking.save()

    return redirect("owner_bookings")

@require_POST
@login_required
def update_booking_status(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        homestay__owner=request.user,
    )

    status = request.POST.get("status")

    if status in [
        "pending",
        "confirmed",
        "cancelled",
        "completed",
    ]:
        booking.status = status
        booking.save()

    return redirect("owner_bookings")
