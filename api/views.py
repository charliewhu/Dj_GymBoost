from django.shortcuts import render
from rest_framework import viewsets

from exercises.models import Exercise

from .serializers import ExerciseSerializer

# Create your views here.
class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
