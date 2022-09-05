from django.test import TestCase

from workouts.forms import WorkoutExerciseSetForm


class WorkoutExerciseSetFormTest(TestCase):
    def test_form_placeholders(self):
        form = WorkoutExerciseSetForm()
        self.assertIn('placeholder="Weight"', form.as_p())
        self.assertIn('placeholder="Reps"', form.as_p())
        self.assertIn('placeholder="RIR"', form.as_p())

    def test_form_validation(self):
        form = WorkoutExerciseSetForm(data={"weight": "", "reps": "", "rir": ""})
        self.assertFalse(form.is_valid())

    def test_weight_validation(self):
        form = WorkoutExerciseSetForm(data={"weight": "-10", "reps": "10", "rir": "3"})
        self.assertFalse(form.is_valid())

    def test_rep_validation(self):
        form = WorkoutExerciseSetForm(data={"weight": "100", "reps": "-3", "rir": "3"})
        self.assertFalse(form.is_valid())

    def test_rir_validation(self):
        form = WorkoutExerciseSetForm(data={"weight": "100", "reps": "5", "rir": "7"})
        self.assertFalse(form.is_valid())

        form = WorkoutExerciseSetForm(data={"weight": "100", "reps": "5", "rir": "-2"})
        self.assertFalse(form.is_valid())

    def test_form_field_type_is_tel(self):
        form = WorkoutExerciseSetForm()
        self.assertEqual(form.fields["weight"].widget.input_type, "tel")
        self.assertEqual(form.fields["reps"].widget.input_type, "tel")
        self.assertEqual(form.fields["rir"].widget.input_type, "tel")
