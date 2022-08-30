from django.test import TestCase
from django.urls import resolve

from .. import views
from ..models import Workout, WorkoutExercise, WorkoutExerciseSet
from exercises.models import Exercise


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve("/")
        self.assertEqual(found.func, views.home)

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


class WorkoutExerciseCreateDeleteTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()
        self.exercise = Exercise.objects.create(name="testex")

    def test_POST_redirects_to_workout(self):
        response = self.client.post(
            "/workout_exercises/create/", data={"workout_id": 1, "exercise_id": 1}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/workouts/1/")

    def test_POST_creates_workout_exercise(self):
        self.client.post(
            "/workout_exercises/create/", data={"workout_id": 1, "exercise_id": 1}
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


class WorkoutExerciseTest(TestCase):
    def setUp(self):
        self.url = "/workout_exercise/1/sets/"
        self.workout = Workout.objects.create()
        self.exercise = Exercise.objects.create(name="testex")
        self.workout_exercise = WorkoutExercise.objects.create(
            workout=self.workout, exercise=self.exercise
        )

    def test_url_resolves_to_correct_view(self):
        found = resolve(self.url)
        self.assertEqual(found.func, views.workout_exercise)

    def test_returns_correct_html(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "workouts/workout_exercise.html")

    def test_exercise_context(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.context["workout_exercise"], WorkoutExercise)

    def test_POST_redirects(self):
        response = self.client.post(
            "/workout_exercise_sets/create/", data={"workout_exercise_id": 1}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], self.url)

    def test_POST_creates_object(self):
        self.client.post(
            "/workout_exercise_sets/create/", data={"workout_exercise_id": 1}
        )
        self.assertEqual(WorkoutExerciseSet.objects.count(), 1)

    def test_weight_reps_in_context(self):
        WorkoutExerciseSet.objects.create(
            workout_exercise=self.workout_exercise, weight=100, reps=10
        )
        response = self.client.get(self.url)
        self.assertQuerysetEqual(
            response.context["sets"], WorkoutExerciseSet.objects.all(), ordered=False
        )
