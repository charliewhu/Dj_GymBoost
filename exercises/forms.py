from django import forms

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ("name",)
        widgets = {
            "name": forms.fields.TextInput(
                attrs={
                    "placeholder": "Exercise Name",
                }
            ),
        }
