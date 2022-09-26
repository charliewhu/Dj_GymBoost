import json
from rest_framework.test import APITestCase

from exercises.models import Exercise
from exercises.tests.factory import ExerciseFactory


class ExerciseTest(APITestCase):
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
            {"name": exercise_name},
        )
        exercise = Exercise.objects.first()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(exercise.name, exercise_name)

    def test_GET_single_object(self):
        self.exercise = ExerciseFactory()
        res = self.client.get(self.url + "1/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res["content-type"], "application/json")
        self.assertEqual(
            json.loads(res.content.decode("utf8")),
            {"id": self.exercise.id, "name": self.exercise.name},
        )

    def test_PUT_object(self):
        self.exercise = ExerciseFactory()
        new_name = "newName"
        res = self.client.put(
            self.url + "1/",
            {"name": new_name},
        )
        exercise = Exercise.objects.first()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(exercise.name, new_name)

    def test_DELETE_object(self):
        self.exercise = ExerciseFactory()
        res = self.client.delete(self.url + "1/")
        exercises = Exercise.objects.count()

        self.assertEqual(res.status_code, 204)
        self.assertEqual(exercises, 0)
