from django.test import TestCase
from django.urls import resolve, reverse

from .factory import RoutineFactory

from ..forms import RoutineForm
from ..models import Routine


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

    def test_routines_list_in_context(self):
        routines = Routine.objects.all()
        self.assertQuerysetEqual(
            self.response.context["routines"], routines, ordered=False
        )


class RoutineDetailTest(TestCase):
    def setUp(self):
        self.routine = RoutineFactory()
        self.response = self.client.get(self.routine.get_absolute_url())

    def test_renders_html(self):
        self.assertTemplateUsed(self.response, "routines/routine.html")

    def test_context_in_response(self):
        self.assertEqual(
            self.response.context["title"],
            self.routine.name,
        )


class RoutineCreateTest(TestCase):
    def setUp(self):
        self.response = self.client.post(
            reverse("routine_create"), data={"name": "new item"}
        )

    def test_redirects_to_routine(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertRegex(self.response["location"], "/routines/1/")

    def test_post_creates_object(self):
        self.assertEqual(Routine.objects.count(), 1)
        self.assertEqual(Routine.objects.get(id=1).name, "new item")
