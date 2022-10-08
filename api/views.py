from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from exercises.models import Exercise
from routines.models import Routine, RoutineExercise
from workouts.models import Workout, WorkoutExercise, WorkoutExerciseSet

from .serializers import (
    ExerciseSerializer,
    RoutineSerializer,
    RoutineExerciseSerializer,
    WorkoutSerializer,
    WorkoutExerciseSerializer,
    WorkoutExerciseSetSerializer,
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


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()


class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutExerciseSerializer
    queryset = WorkoutExercise.objects.all()


class WorkoutExerciseSetViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutExerciseSetSerializer
    queryset = WorkoutExerciseSet.objects.all()


@api_view(["POST"])
def routine_workout(request, pk):
    if request.method == "POST":
        routine = Routine.objects.get(id=pk)
        workout = routine.create_workout()
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
