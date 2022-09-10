from django.test import TestCase

from exercises.tests.factory import ExerciseFactory
from .factory import RoutineExerciseFactory, RoutineFactory
from ..models import Routine, RoutineExercise
from workouts.models import Workout


class RoutineModelTest(TestCase):
    def test_saving_item(self):
        routine = Routine()
        routine.name = "Test Routine"
        routine.save()

        self.assertEqual(Routine.objects.count(), 1)
        self.assertEqual(Routine.objects.get(id=1).name, "Test Routine")

    def test_create_workout(self):
        self.routine = RoutineFactory()
        self.exercise = ExerciseFactory()
        self.routine_exercise = RoutineExerciseFactory(
            routine=self.routine, exercise=self.exercise
        )

        self.workout = self.routine.create_workout()

        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(
            self.workout.exercises.first().exercise,
            self.routine.exercises.first().exercise,
        )
        self.assertEqual(self.workout, Workout.objects.first())


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
