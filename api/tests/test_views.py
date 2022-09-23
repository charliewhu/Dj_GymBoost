import json
from django.test import TestCase

from exercises.tests.factory import ExerciseFactory


class ExerciseTest(TestCase):
    def setUp(self):
        self.exercise = ExerciseFactory()

    def test_get_returns_json_200(self):
        res = self.client.get("/api/exercises/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content.decode("utf8")),
            [
                {"id": self.exercise.id, "name": self.exercise.name},
                {"id": self.exercise.id, "name": self.exercise.name},
            ],
        )
