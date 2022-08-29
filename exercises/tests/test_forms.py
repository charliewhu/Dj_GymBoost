from django.test import TestCase

from exercises.forms import ExerciseForm


class ExerciseFormTest(TestCase):
    def test_form_placeholders(self):
        form = ExerciseForm()
        self.assertIn('placeholder="Exercise Name"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ExerciseForm(data={"name": ""})
        self.assertFalse(form.is_valid())
