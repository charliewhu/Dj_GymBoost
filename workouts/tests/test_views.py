from django.test import TestCase
from django.urls import resolve, reverse

from workouts.tests.factory import WorkoutExerciseFactory, WorkoutExerciseSetFactory

from .. import views
from ..models import Workout, WorkoutExercise, WorkoutExerciseSet
from ..forms import WorkoutExerciseSetForm
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


class WorkoutsTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()
        self.response = self.client.get("/workouts/")

    def test_GET_renders_template(self):
        self.assertTemplateUsed(self.response, "workouts/workouts.html")

    def test_GET_has_workouts_in_context(self):
        workouts = Workout.objects.all()
        self.assertQuerysetEqual(
            self.response.context["workouts"], workouts, ordered=False
        )

    def test_POST_creates_workout(self):
        self.client.post("/workouts/")
        self.assertEqual(Workout.objects.count(), 2)

    def test_POST_causes_redirect(self):
        response = self.client.post("/workouts/")
        self.assertEqual(response.status_code, 302)
        self.assertRegex(response["location"], "workouts/(\d+)/")


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


class WorkoutDeleteTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()

    def test_POST_delete_workout_url_redirects_to_workouts(self):
        response = self.client.post("/workouts/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/workouts/")

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
        self.workout_exercise = WorkoutExerciseSetFactory()
        self.response = self.client.get(self.url)

    def test_url_resolves_to_correct_view(self):
        found = resolve(self.url)
        self.assertEqual(found.func, views.workout_exercise)

    def test_returns_correct_html(self):
        self.assertTemplateUsed(self.response, "workouts/workout_exercise.html")

    def test_context(self):
        self.assertIsInstance(
            self.response.context["workout_exercise"], WorkoutExercise
        )
        self.assertQuerysetEqual(
            self.response.context["sets"],
            WorkoutExerciseSet.objects.all(),
            ordered=False,
        )

    def test_renders_form(self):
        self.assertIsInstance(self.response.context["form"], WorkoutExerciseSetForm)

    def test_renders_prefilled_form(self):
        response = self.client.get(self.url, data={"id": 1, "weight": 100, "reps": 10})
        self.assertIn("100", response.content.decode())
        self.assertIn("10", response.content.decode())

    def test_workout_exercise_set_in_context_if_id_in_GET(self):
        response = self.client.get(self.url, data={"id": 1, "weight": 100, "reps": 10})
        self.assertIsInstance(
            response.context["workout_exercise_set"], WorkoutExerciseSet
        )


class WorkoutExerciseSetCreateTest(TestCase):
    def setUp(self):
        self.url = "/workout_exercise_sets/create/"
        self.workout_exercise = WorkoutExerciseFactory()

    def test_POST_redirects(self):
        response = self.client.post(
            self.url,
            data={"workout_exercise_id": 1, "weight": 20, "reps": 10},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/workout_exercise/1/sets/")

    def test_POST_creates_object(self):
        self.client.post(
            self.url,
            data={"workout_exercise_id": 1, "weight": 20, "reps": 10},
        )
        self.assertEqual(WorkoutExerciseSet.objects.count(), 1)
        set_ = WorkoutExerciseSet.objects.first()
        self.assertEqual(set_.weight, 20)
        self.assertEqual(set_.reps, 10)


class WorkoutExerciseSetUpdateTest(TestCase):
    def setUp(self):
        self.wes = WorkoutExerciseSetFactory()
        self.response = self.client.post(
            reverse("workout_exercise_set_update", args=[self.wes.id]),
            data={"weight": 20, "reps": 10},
        )

    def test_POST_redirects_to_WorkoutExercise(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(
            self.response["location"], self.wes.workout_exercise.get_absolute_url()
        )

    def test_POST_updates_object(self):
        wes = WorkoutExerciseSet.objects.first()
        self.assertEqual(wes.weight, 20.0)
        self.assertEqual(wes.reps, 10)


class WorkoutExerciseSetDeleteTest(TestCase):
    def setUp(self):
        self.wes = WorkoutExerciseSetFactory()
        self.response = self.client.post(
            reverse("workout_exercise_set_delete", args=[self.wes.id])
        )

    def test_POST_redirects_to_WorkoutExercise(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(
            self.response["location"], self.wes.workout_exercise.get_absolute_url()
        )

    def test_POST_deletes_object(self):
        self.assertEqual(WorkoutExerciseSet.objects.count(), 0)
