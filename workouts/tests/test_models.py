from django.test import TestCase

from exercises.models import Exercise
from ..models import Workout, WorkoutExercise


class WorkoutTest(TestCase):
    def test_get_absolute_url(self):
        workout = Workout.objects.create()
        self.assertEqual(workout.get_absolute_url(), f"/workouts/{workout.id}/")


class WorkoutExerciseTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()
        self.exercise = Exercise.objects.create(name="testex")

    def test_saving_workout_exercise(self):
        workout_exercise = WorkoutExercise()
        workout_exercise.workout = self.workout
        workout_exercise.exercise = self.exercise
        workout_exercise.save()

        workout_exercise = WorkoutExercise.objects.first()

        self.assertEqual(workout_exercise.workout, self.workout)
        self.assertEqual(workout_exercise.exercise, self.exercise)
