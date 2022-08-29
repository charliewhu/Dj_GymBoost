from django.test import TestCase
from django.urls import resolve

from ..models import Exercise


class ExerciseModelTest(TestCase):
    def test_saving_item(self):
        exercise = Exercise()
        exercise.name = "Test Exercise"
        exercise.save()

        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(Exercise.objects.get(id=1).name, "Test Exercise")
