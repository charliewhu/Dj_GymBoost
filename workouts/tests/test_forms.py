from django.test import TestCase

from workouts.forms import WorkoutExerciseSetForm


class WorkoutExerciseSetFormTest(TestCase):
    def test_form_placeholders(self):
        form = WorkoutExerciseSetForm()
        self.assertIn('placeholder="Weight"', form.as_p())
        self.assertIn('placeholder="Reps"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = WorkoutExerciseSetForm(data={"weight": "", "reps": ""})
        self.assertFalse(form.is_valid())

        form = WorkoutExerciseSetForm(data={"weight": "200", "reps": ""})
        self.assertFalse(form.is_valid())

        form = WorkoutExerciseSetForm(data={"weight": "", "reps": "10"})
        self.assertFalse(form.is_valid())

    def test_form_field_type_is_tel(self):
        form = WorkoutExerciseSetForm()
        self.assertEqual(form.fields["weight"].widget.input_type, "tel")
        self.assertEqual(form.fields["reps"].widget.input_type, "tel")
