from django.test import TestCase
from django.urls import resolve

from ..models import Exercise
from ..views import exercises
from ..forms import ExerciseForm


class ExercisePageTest(TestCase):
    def setUp(self):
        self.ex = Exercise.objects.create(name="test exercise")
        self.response = self.client.get("/exercises/")

    def test_url_resolves_to_exercise_view(self):
        found = resolve("/exercises/")
        self.assertEqual(found.func, exercises)

    def test_url_returns_correct_html(self):
        self.assertTemplateUsed(self.response, "exercises/exercises.html")

    def test_exercises_page_lists_exercises(self):
        self.assertIn(self.ex.name, self.response.content.decode())

    def test_renders_form(self):
        self.assertIsInstance(self.response.context["form"], ExerciseForm)

    def test_invalid_POST_doesnt_create_object(self):
        response = self.client.post("/exercises/", data={"name": ""})
        self.assertEqual(Exercise.objects.count(), 1)

    def test_POST_creates_object(self):
        response = self.client.post("/exercises/", data={"name": "new item"})
        self.assertEqual(Exercise.objects.count(), 2)
        self.assertEqual(Exercise.objects.get(id=2).name, "new item")
