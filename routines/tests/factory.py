from factory.django import DjangoModelFactory
from factory import SubFactory


class RoutineFactory(DjangoModelFactory):
    class Meta:
        model = "routines.Routine"

    name = "test routine"
