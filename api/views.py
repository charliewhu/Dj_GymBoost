from django.shortcuts import render
from rest_framework import viewsets

from exercises.models import Exercise
from routines.models import Routine

from .serializers import ExerciseSerializer, RoutineSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class RoutineViewSet(viewsets.ModelViewSet):
    serializer_class = RoutineSerializer
    queryset = Routine.objects.all()
