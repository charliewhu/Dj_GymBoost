import json
from django.test import TestCase

from exercises.models import Exercise
from exercises.tests.factory import ExerciseFactory


class ExerciseTest(TestCase):
    def setUp(self):
        self.url = "/api/exercises/"

    def test_GET(self):
        self.exercise = ExerciseFactory()
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content.decode("utf8")),
            [
                {"id": self.exercise.id, "name": self.exercise.name},
            ],
        )

    def test_POSTing_a_new_item(self):
        exercise_name = "new exercise"
        response = self.client.post(
            self.url,
            {"name": "new exercise"},
        )
        exercise = Exercise.objects.first()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(exercise.name, exercise_name)
