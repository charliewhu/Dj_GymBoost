from django.test import TestCase
from django.urls import resolve, reverse

from workouts.models import WorkoutExercise

from .factory import RoutineFactory, RoutineExerciseFactory
from exercises.tests.factory import ExerciseFactory

from ..forms import RoutineForm
from ..models import Routine, RoutineExercise


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

    def test_context(self):
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

    def test_object_in_context(self):
        self.assertEqual(self.response.context["routine"], self.routine)

    def test_routine_exercises_in_context(self):
        routine_exercise = RoutineExerciseFactory(routine=self.routine)
        self.response = self.client.get(self.routine.get_absolute_url())
        self.assertQuerysetEqual(
            self.response.context["routine_exercises"],
            RoutineExercise.objects.filter(routine=routine_exercise.routine),
            ordered=False,
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


class RoutineDeleteTest(TestCase):
    def setUp(self):
        self.routine = RoutineFactory()
        self.response = self.client.post(
            reverse("routine_delete", args=[self.routine.id])
        )

    def test_redirect(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response["location"], "/routines/")

    def test_deletes_objects(self):
        self.assertEqual(Routine.objects.count(), 0)


class RoutineExerciseCreateTest(TestCase):
    def setUp(self):
        self.routine = RoutineFactory()
        self.exercise = ExerciseFactory()
        self.response = self.client.post(
            reverse("routine_exercise_create"), data={"routine_id": 1, "exercise_id": 1}
        )

    def test_creates_objects(self):
        self.assertEqual(RoutineExercise.objects.all().count(), 1)

    def test_redirects(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response["location"], "/routines/1/")


class RoutineExerciseDeleteTest(TestCase):
    def setUp(self):
        self.routine_exercise = RoutineExerciseFactory()
        self.response = self.client.post(
            reverse("routine_exercise_delete", args=[self.routine_exercise.id])
        )

    def test_redirect(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response["location"], "/routines/1/")

    def test_deletes_object(self):
        self.assertEqual(RoutineExercise.objects.count(), 0)


class RoutineWorkoutCreateTest(TestCase):
    def setUp(self):
        RoutineExerciseFactory()
        self.response = self.client.post(
            reverse("routine_workout_create", kwargs={"pk": 1})
        )

    def test_redirect_to_workout(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response["location"], "/workouts/1/")

    def test_create_workout_with_exercises(self):
        self.assertEqual(
            WorkoutExercise.objects.count(), RoutineExercise.objects.count()
        )
