import json
from rest_framework.test import APITestCase

from exercises.tests.factory import ExerciseFactory
from routines.tests.factory import RoutineFactory

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