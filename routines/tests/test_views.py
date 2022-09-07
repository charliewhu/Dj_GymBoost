from django.test import TestCase
from django.urls import resolve, reverse

from ..forms import RoutineForm


class RoutinesListTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse("routines"))

    def test_renders_correct_html(self):
        self.assertTemplateUsed(self.response, "routines/routines.html")

    def test_context_in_response(self):
        self.assertEqual(
            self.response.context["title"],
            "Routines",
        )

    def test_renders_form(self):
        self.assertIsInstance(self.response.context["form"], RoutineForm)
