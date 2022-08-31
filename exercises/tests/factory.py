from factory.django import DjangoModelFactory
from factory import SubFactory


class ExerciseFactory(DjangoModelFactory):
    class Meta:
        model = "exercises.Exercise"

    name = "test exercise"
