import json
from rest_framework.test import APITestCase

from exercises.tests.factory import ExerciseFactory
from routines.tests.factory import RoutineFactory, RoutineExerciseFactory
from workouts.models import Workout, WorkoutExercise, WorkoutExerciseSet
from workouts.tests.factory import (
    WorkoutExerciseFactory,
    WorkoutExerciseSetFactory,
    WorkoutFactory,
)


class ExerciseTest(APITestCase):
    def setUp(self):
        self.url = "/api/exercises/"
        self.exercise = ExerciseFactory()

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content.decode("utf8")),
            [
                {"id": self.exercise.id, "name": self.exercise.name},
            ],
        )


class RoutineTest(APITestCase):
    def setUp(self):
        self.url = "/api/routines/"
        self.routine = RoutineFactory()

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content.decode("utf8")),
            [
                {"id": self.routine.id, "name": self.routine.name},
            ],
        )


class RoutineExerciseTest(APITestCase):
    def setUp(self):
        self.url = "/api/routineexercises/"
        self.routine_exercise = RoutineExerciseFactory()

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content.decode("utf8")),
            [
                {
                    "id": self.routine_exercise.id,
                    "routine": self.routine_exercise.routine.id,
                    "exercise": self.routine_exercise.exercise.id,
                    "name": self.routine_exercise.exercise.name,
                },
            ],
        )


class WorkoutTest(APITestCase):
    def setUp(self):
        self.url = "/api/workouts/"
        self.workout_exercise_set = WorkoutExerciseSetFactory()

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")


class WorkoutExerciseTest(APITestCase):
    def setUp(self):
        self.url = "/api/workoutexercises/"
        self.workout_exercise = WorkoutExerciseFactory()
        self.workout_exercise_set = WorkoutExerciseSetFactory(
            workout_exercise=self.workout_exercise
        )

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content),
            [
                {
                    "id": self.workout_exercise.id,
                    "created_on": self.workout_exercise.created_on.isoformat().replace(
                        "+00:00", "Z"
                    ),
                    "workout": self.workout_exercise.workout.id,
                    "exercise": self.workout_exercise.exercise.id,
                    "name": self.workout_exercise.exercise.name,
                },
            ],
        )


class WorkoutExerciseSetTest(APITestCase):
    def setUp(self):
        self.url = "/api/workoutexercisesets/"
        self.workout_exercise_set = WorkoutExerciseSetFactory()

    def test_GET(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content),
            [
                {
                    "id": self.workout_exercise_set.id,
                    "workout_exercise": self.workout_exercise_set.workout_exercise.id,
                    "weight": self.workout_exercise_set.weight,
                    "reps": self.workout_exercise_set.reps,
                    "rir": self.workout_exercise_set.rir,
                },
            ],
        )


class RoutineWorkoutTest(APITestCase):
    def setUp(self):
        self.routine = RoutineFactory()
        self.routine_exercise = RoutineExerciseFactory(routine=self.routine)
        self.url = f"/api/routines/{self.routine.id}/workout/"

    def test_POST(self):
        res = self.client.post(self.url)
        self.assertEqual(res.status_code, 201)

        self.workout = Workout.objects.first()
        self.assertEqual(json.loads(res.content.decode("utf8"))["id"], 1)
        self.assertEqual(
            json.loads(res.content.decode("utf8"))["routine_name"], self.routine.name
        )


class WorkoutExerciseDeleteRelatedSetsTest(APITestCase):
    def setUp(self):
        self.workout_exercise = WorkoutExerciseFactory()
        self.set1 = WorkoutExerciseSetFactory(workout_exercise=self.workout_exercise)
        self.set2 = WorkoutExerciseSetFactory(workout_exercise=self.workout_exercise)
        self.url = f"/api/workoutexercises/{self.workout_exercise.id}/delete_sets/"

    def test_DELETE(self):
        self.assertEqual(WorkoutExerciseSet.objects.count(), 2)
        res = self.client.delete(self.url)

        self.assertEqual(res.status_code, 204)
        self.assertEqual(WorkoutExerciseSet.objects.count(), 0)
        self.assertEqual(WorkoutExercise.objects.count(), 1)
