from django.db import models
from django.urls import reverse

from exercises.models import Exercise
from workouts.models import Workout, WorkoutExercise

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("routine", kwargs={"pk": self.pk})

    def create_workout(self):
        workout = Workout.objects.create()
        for routine_exercise in self.exercises.all():
            WorkoutExercise.objects.create(
                workout=workout, exercise=routine_exercise.exercise
            )
        return workout


class RoutineExercise(models.Model):
    routine = models.ForeignKey(
        Routine, related_name="exercises", on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
