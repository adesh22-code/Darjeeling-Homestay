from .models import Homestay, Booking
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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


def home(request):
    homestays = Homestay.objects.all()

    return render(
        request,
        "homestays/home.html",
        {
            "homestays": homestays
        }
    )




@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).select_related(
        "homestay"
    ).order_by("-created_at")

    return render(
        request,
        "homestays/my_bookings.html",
        {
            "bookings": bookings,
        },
    )



@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    if booking.status == "pending":
        booking.status = "cancelled"
        booking.save()

    return redirect("my_bookings")



def homestay_detail(request, id):
    homestay = get_object_or_404(Homestay, id=id)

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.homestay = homestay

            # Link booking to logged-in user
            if request.user.is_authenticated:
                booking.user = request.user

            # Validate maximum guests
            if booking.guests > homestay.max_guests:
                form.add_error(
                    "guests",
                    f"This homestay allows a maximum of {homestay.max_guests} guests."
                )

            else:
                booking.save()

                return render(
                    request,
                    "homestays/booking_success.html",
                    {
                        "booking": booking
                    }
                )

    else:
        form = BookingForm()

    return render(
        request,
        "homestays/detail.html",
        {
            "homestay": homestay,
            "form": form,
        }
    )
