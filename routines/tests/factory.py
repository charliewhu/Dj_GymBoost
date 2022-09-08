from factory.django import DjangoModelFactory
from factory import SubFactory

from exercises.tests.factory import ExerciseFactory


class RoutineFactory(DjangoModelFactory):
    class Meta:
        model = "routines.Routine"

    name = "test routine"


class RoutineExerciseFactory(DjangoModelFactory):
    class Meta:
        model = "routines.RoutineExercise"

    routine = SubFactory(RoutineFactory)
    exercise = SubFactory(ExerciseFactory)
