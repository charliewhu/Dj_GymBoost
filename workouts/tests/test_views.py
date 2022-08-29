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

    def test_workouts_in_context(self):
        Workout.objects.create()
        Workout.objects.create()
        workouts = Workout.objects.all()

        response = self.client.get("/")

        self.assertQuerysetEqual(response.context["workouts"], workouts, ordered=False)


class WorkoutTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()

    def test_workout_in_context(self):
        response = self.client.get(self.workout.get_absolute_url())
        self.assertIsInstance(response.context["workout"], Workout)

    def test_workout_exercises_in_context(self):
        exercise = Exercise.objects.create(name="testex")
        workout_exercise = WorkoutExercise.objects.create(
            workout=self.workout,
            exercise=exercise,
        )

        response = self.client.get(self.workout.get_absolute_url())
        self.assertEqual(response.context["workout_exercises"][0], workout_exercise)

    def test_POST_creates_workout(self):
        self.client.post("/workouts/")
        self.assertEqual(Workout.objects.count(), 2)

    def test_POST_causes_redirect(self):
        response = self.client.post("/workouts/")
        self.assertEqual(response.status_code, 302)
        self.assertRegex(response["location"], "workouts/(\d+)/")

    def test_POST_delete_workout_url_redirects_to_home(self):
        response = self.client.post("/workouts/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/")

    def test_POST_delete_workout_url_deletes_object(self):
        self.client.post("/workouts/1/delete/")
        self.assertEqual(Workout.objects.count(), 0)


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
