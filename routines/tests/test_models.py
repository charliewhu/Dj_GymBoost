from django.test import TestCase

from ..models import Routine


class RoutineModelTest(TestCase):
    def test_saving_item(self):
        routine = Routine()
        routine.name = "Test Routine"
        routine.save()

        self.assertEqual(Routine.objects.count(), 1)
        self.assertEqual(Routine.objects.get(id=1).name, "Test Routine")
