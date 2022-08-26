from django.test import TestCase

from .models import Exercise

# Create your tests here.
class ExerciseModelTest(TestCase):
    def test_saving_item(self):
        exercise = Exercise()
        exercise.name = "Test Exercise"
        exercise.save()

        self.assertEqual(Exercise.objects.count(), 1)
        self.assertEqual(Exercise.objects.get(id=1).name, "Test Exercise")
