from factory.django import DjangoModelFactory
from factory import SubFactory

from exercises.tests.factory import ExerciseFactory


class WorkoutFactory(DjangoModelFactory):
    class Meta:
        model = "workouts.Workout"


class WorkoutExerciseFactory(DjangoModelFactory):
    class Meta:
        model = "workouts.WorkoutExercise"

    workout = SubFactory(WorkoutFactory)
    exercise = SubFactory(ExerciseFactory)


class WorkoutExerciseSetFactory(DjangoModelFactory):
    class Meta:
        model = "workouts.WorkoutExerciseSet"

    workout_exercise = SubFactory(WorkoutExerciseFactory)
    weight = 100
    reps = 10
