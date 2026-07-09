from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Homestay, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "guest_name",
            "guest_email",
            "guest_phone",
            "check_in",
            "check_out",
            "guests",
        ]

        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date"}),
            "check_out": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out:

            # Check-in cannot be in the past
            if check_in < timezone.localdate():
                raise ValidationError(
                    "Check-in date cannot be in the past."
                )

            # Check-out must be after check-in
            if check_out <= check_in:
                raise ValidationError(
                    "Check-out date must be after the check-in date."
                )

        return cleaned_data


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = [
            "rating",
            "comment",
        ]

        widgets = {
            "rating": forms.Select(
                choices=[
                    (1, "⭐ 1"),
                    (2, "⭐⭐ 2"),
                    (3, "⭐⭐⭐ 3"),
                    (4, "⭐⭐⭐⭐ 4"),
                    (5, "⭐⭐⭐⭐⭐ 5"),
                ]
            ),
            "comment": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Write your experience..."
                }
            ),
        }
