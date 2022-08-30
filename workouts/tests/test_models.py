from django.test import TestCase

from exercises.models import Exercise
from ..models import Workout, WorkoutExercise, WorkoutExerciseSet


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

    def test_get_absolute_url(self):
        workout_exercise = WorkoutExercise.objects.create(
            workout=self.workout, exercise=self.exercise
        )
        self.assertEqual(
            workout_exercise.get_absolute_url(),
            f"/workout_exercise/{workout_exercise.id}/sets/",
        )


class WorkoutExerciseSetTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create()
        self.exercise = Exercise.objects.create(name="testex")
        self.workout_exercise = WorkoutExercise.objects.create(
            workout=self.workout, exercise=self.exercise
        )

    def test_saving_workout_exercise_set(self):
        workout_exercise_set = WorkoutExerciseSet()
        workout_exercise_set.workout_exercise = self.workout_exercise
        workout_exercise_set.weight = 100
        workout_exercise_set.reps = 10
        workout_exercise_set.save()

        self.assertEqual(workout_exercise_set.workout_exercise, self.workout_exercise)
        self.assertIsInstance(workout_exercise_set, WorkoutExerciseSet)

        set_ = WorkoutExerciseSet.objects.first()
        self.assertEqual(set_.workout_exercise, self.workout_exercise)
        self.assertEqual(set_.weight, 100)
        self.assertEqual(set_.reps, 10)
