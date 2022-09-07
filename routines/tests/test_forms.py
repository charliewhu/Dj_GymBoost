from django.test import TestCase

from ..forms import RoutineForm


class RoutineFormTest(TestCase):
    def test_form_placeholders(self):
        form = RoutineForm()
        self.assertIn('placeholder="Routine Name"', form.as_p())

    def RoutineForm(self):
        form = RoutineForm(data={"name": ""})
        self.assertFalse(form.is_valid())
