from django import forms

from .models import WorkoutExerciseSet


class WorkoutExerciseSetForm(forms.ModelForm):
    class Meta:
        model = WorkoutExerciseSet
        fields = (
            "weight",
            "reps",
        )
        widgets = {
            "weight": forms.fields.NumberInput(
                attrs={
                    "placeholder": "Weight",
                }
            ),
            "reps": forms.fields.NumberInput(
                attrs={
                    "placeholder": "Reps",
                }
            ),
        }
