from django.test import TestCase
from django.urls import resolve, reverse
from django.http import HttpRequest

from .views import home
from .models import Workout, WorkoutExercise
from exercises.models import Exercise

# Create your tests here.
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
    def test_get_absolute_url(self):
        workout = Workout.objects.create()
        self.assertEqual(workout.get_absolute_url(), f"/workouts/{workout.id}/")

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
    def test_POST_redirects_to_workout(self):
        Workout.objects.create()
        Exercise.objects.create(name="testex")

        response = self.client.post(
            "/workout_exercises/", data={"workout_id": 1, "exercise_id": 1}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/workouts/1/")

    def test_POST_creates_workout_exercise(self):
        Workout.objects.create()
        Exercise.objects.create(name="testex")

        self.client.post(
            "/workout_exercises/", data={"workout_id": 1, "exercise_id": 1}
        )

        self.assertEqual(WorkoutExercise.objects.count(), 1)

    def test_saving_workout_exercise(self):
        workout = Workout.objects.create()
        exercise = Exercise.objects.create(name="test exercise")
        workout_exercise = WorkoutExercise()
        workout_exercise.workout = workout
        workout_exercise.exercise = exercise
        workout_exercise.save()

        workout_exercise = WorkoutExercise.objects.first()

        self.assertEqual(workout_exercise.workout, workout)
        self.assertEqual(workout_exercise.exercise, exercise)
