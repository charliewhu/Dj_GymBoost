from django import forms

from .models import WorkoutExerciseSet


class PhoneInput(forms.fields.TextInput):
    input_type = "tel"


class WorkoutExerciseSetForm(forms.ModelForm):
    class Meta:
        model = WorkoutExerciseSet
        fields = (
            "weight",
            "reps",
        )
        widgets = {
            "weight": PhoneInput(
                attrs={
                    "placeholder": "Weight",
                }
            ),
            "reps": PhoneInput(
                attrs={
                    "placeholder": "Reps",
                }
            ),
        }
