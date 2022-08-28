from django.test import TestCase
from django.urls import resolve

from ..views import home
from ..models import Workout, WorkoutExercise
from exercises.models import Exercise


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_POST_creates_workout(self):
        self.client.post("/")
        self.assertEqual(Workout.objects.count(), 1)

    def test_POST_causes_redirect(self):
        response = self.client.post("/")
        self.assertEqual(response.status_code, 302)
        self.assertRegex(response["location"], "workouts/(\d+)/")


class WorkoutTest(TestCase):
    def test_workout_in_context(self):
        workout = Workout.objects.create()
        response = self.client.get(workout.get_absolute_url())
        self.assertIsInstance(response.context["workout"], Workout)

    def test_workout_exercises_in_context(self):
        workout = Workout.objects.create()
        exercise = Exercise.objects.create(name="testex")
        workout_exercise = WorkoutExercise.objects.create(
            workout=workout,
            exercise=exercise,
        )

        response = self.client.get(workout.get_absolute_url())
        self.assertEqual(response.context["workout_exercises"][0], workout_exercise)


class WorkoutExerciseTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()
        self.exercise = Exercise.objects.create(name="testex")

    def test_POST_redirects_to_workout(self):
        response = self.client.post(
            "/workout_exercises/", data={"workout_id": 1, "exercise_id": 1}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/workouts/1/")

    def test_POST_creates_workout_exercise(self):
        self.client.post(
            "/workout_exercises/", data={"workout_id": 1, "exercise_id": 1}
        )

        self.assertEqual(WorkoutExercise.objects.count(), 1)

    def test_POST_delete_workout_exercise_url_redirects_to_workout(self):
        WorkoutExercise.objects.create(workout=self.workout, exercise=self.exercise)
        response = self.client.post("/workout_exercises/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/workouts/1/")

    def test_POST_delete_workout_exercise_url_deletes_object(self):
        WorkoutExercise.objects.create(workout=self.workout, exercise=self.exercise)
        self.client.post("/workout_exercises/1/delete/")
        self.assertEqual(WorkoutExercise.objects.count(), 0)
