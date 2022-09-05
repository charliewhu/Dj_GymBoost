from django import forms

from crispy_forms.helper import FormHelper

from .models import WorkoutExerciseSet


class PhoneInput(forms.fields.TextInput):
    input_type = "tel"


class WorkoutExerciseSetForm(forms.ModelForm):
    class Meta:
        model = WorkoutExerciseSet
        fields = ("weight", "reps", "rir")
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
            "rir": PhoneInput(
                attrs={
                    "placeholder": "RIR",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
