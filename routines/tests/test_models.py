from django.test import TestCase

from exercises.tests.factory import ExerciseFactory
from .factory import RoutineFactory
from ..models import Routine, RoutineExercise


class RoutineModelTest(TestCase):
    def test_saving_item(self):
        routine = Routine()
        routine.name = "Test Routine"
        routine.save()

        self.assertEqual(Routine.objects.count(), 1)
        self.assertEqual(Routine.objects.get(id=1).name, "Test Routine")


class RoutineExerciseTest(TestCase):
    def setUp(self):
        self.routine = RoutineFactory()
        self.exercise = ExerciseFactory()

    def test_save(self):
        routine_exercise = RoutineExercise()
        routine_exercise.routine = self.routine
        routine_exercise.exercise = self.exercise
        routine_exercise.save()

        RoutineExercise.objects.first()
        self.assertEqual(routine_exercise.routine, self.routine)
        self.assertEqual(routine_exercise.exercise, self.exercise)
