from django import forms

from .models import Routine


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ("name",)
        widgets = {
            "name": forms.fields.TextInput(
                attrs={
                    "placeholder": "Routine Name",
                }
            ),
        }
