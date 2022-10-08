from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from exercises.models import Exercise

# Create your models here.
class Workout(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    routine = models.ForeignKey(
        "routines.Routine", related_name="workouts", on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse("workout", kwargs={"pk": self.pk})


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, related_name="exercises", on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("workout_exercise", kwargs={"pk": self.pk})


class WorkoutExerciseSet(models.Model):
    workout_exercise = models.ForeignKey(
        WorkoutExercise, related_name="sets", on_delete=models.CASCADE
    )
    weight = models.FloatField(validators=[MinValueValidator(0)])
    reps = models.PositiveSmallIntegerField()
    rir = models.PositiveSmallIntegerField(
        null=True, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
