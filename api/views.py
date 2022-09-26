from django.shortcuts import render
from rest_framework import viewsets

from exercises.models import Exercise
from routines.models import Routine, RoutineExercise

from .serializers import (
    ExerciseSerializer,
    RoutineSerializer,
    RoutineExerciseSerializer,
)


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class RoutineViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineSerializer
    queryset = Routine.objects.all()


class RoutineExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineExerciseSerializer
    queryset = RoutineExercise.objects.all()
