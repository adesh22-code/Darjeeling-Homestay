from django import forms
from .models import Homestay


class HomestayForm(forms.ModelForm):
    class Meta:
        model = Homestay

        exclude = (
            "owner",
        )
