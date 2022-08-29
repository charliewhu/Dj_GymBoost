from django.test import TestCase
from django.urls import resolve

from ..models import Exercise
from ..views import exercises


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
