from django.test import TestCase

from exercises.models import Exercise
from workouts.tests.factory import (
    WorkoutExerciseFactory,
    WorkoutExerciseSetFactory,
    WorkoutFactory,
)
from ..models import Workout, WorkoutExercise, WorkoutExerciseSet


class WorkoutTest(TestCase):
    def setUp(self):
        self.workout = WorkoutFactory()

    def test_get_abstotal_sets(self):
        workout = Workout.objects.create()
        self.assertEqual(workout.get_absolute_url(), f"/workouts/{workout.id}/")

    def test_ttotal_sets(self):
        ex = WorkoutExerciseFactory(workout=self.workout)
        WorkoutExerciseSetFactory(workout_exercise=ex)
        self.assertEqual(self.workout.total_sets(), 1)

    def test_total_volume(self):
        ex = WorkoutExerciseFactory(workout=self.workout)
        set_ = WorkoutExerciseSetFactory(workout_exercise=ex)
        self.assertEqual(self.workout.total_volume(), set_.weight * set_.reps)


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

    def test_get_total_sets(self):
        workout_exercise = WorkoutExerciseFactory()
        set_ = WorkoutExerciseSetFactory(workout_exercise=workout_exercise)
        self.assertEqual(workout_exercise.total_sets(), 1)

    def test_total_volume(self):
        workout_exercise = WorkoutExerciseFactory()
        set_ = WorkoutExerciseSetFactory(workout_exercise=workout_exercise)
        set2 = WorkoutExerciseSetFactory(workout_exercise=workout_exercise)
        self.assertEqual(
            workout_exercise.total_volume(),
            (set_.weight * set_.reps) + (set2.weight * set2.reps),
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

    def test_total_volume(self):
        workout_exercise_set = WorkoutExerciseSetFactory()
        self.assertEqual(
            workout_exercise_set.total_volume(),
            workout_exercise_set.reps * workout_exercise_set.weight,
        )
