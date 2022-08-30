from django.db import models
from django.urls import reverse
from exercises.models import Exercise

# Create your models here.
class Workout(models.Model):
    def get_absolute_url(self):
        return reverse("workout", kwargs={"pk": self.pk})


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, related_name="exercises", on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("workout_exercise", kwargs={"pk": self.pk})
