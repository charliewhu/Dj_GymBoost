from django.db import models
from django.urls import reverse

from exercises.models import Exercise

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("routine", kwargs={"pk": self.pk})


class RoutineExercise(models.Model):
    routine = models.ForeignKey(
        Routine, related_name="exercises", on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
