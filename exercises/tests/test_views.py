from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Exercise
from ..forms import ExerciseForm
from .. import views


class ExerciseTest(TestCase):
    def setUp(self):
        self.ex = Exercise.objects.create(name="test exercise")
        self.response = self.client.get("/exercises/")

    def test_url_resolves_to_exercise_view(self):
        found = resolve("/exercises/")
        self.assertEqual(found.func, views.exercises)

    def test_url_returns_correct_html(self):
        self.assertTemplateUsed(self.response, "exercises/exercises.html")

    def test_exercises_page_lists_exercises(self):
        self.assertIn(self.ex.name, self.response.content.decode())


class ExerciseCreateTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse("exercise_create"))

    def test_url_resolves_to_exercise_view(self):
        found = resolve(reverse("exercise_create"))
        self.assertEqual(found.func, views.exercise_create)

    def test_url_returns_correct_html(self):
        self.assertTemplateUsed(self.response, "exercises/create.html")

    def test_renders_form(self):
        self.assertIsInstance(self.response.context["form"], ExerciseForm)

    def test_invalid_POST_doesnt_create_object(self):
        self.assertEqual(Exercise.objects.count(), 0)

    def test_POST_redirects(self):
        response = self.client.post("/exercises/create/", data={"name": "new item"})
        self.assertEqual(response.status_code, 302)
        self.assertRegex(response["location"], "exercises/")

    def test_POST_creates_object(self):
        self.client.post("/exercises/create/", data={"name": "new item"})
        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(Exercise.objects.get(id=1).name, "new item")

    def test_context_contains_workout_id(self):
        self.response = self.client.get(
            reverse("exercise_create"), data={"workout_id": 1}
        )
        self.assertEqual(self.response.context["workout_id"], "1")

    def test_POST_redirects_if_workout_id_in_data(self):
        response = self.client.post(
            "/exercises/create/", data={"name": "new item", "workout_id": 1}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRegex(response["location"], "/exercises/?workout_id=1/")


class ExerciseDeleteTest(TestCase):
    def setUp(self):
        Exercise.objects.create(name="test")
        self.response = self.client.post("/exercises/1/delete/")

    def test_POST_redirects(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response["location"], "/exercises/")

    def test_POST_deletes_object(self):
        self.assertEqual(Exercise.objects.count(), 0)
