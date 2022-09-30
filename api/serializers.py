from rest_framework import serializers

from exercises.models import Exercise
from routines.models import Routine, RoutineExercise
from workouts.models import Workout


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
        ]


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = [
            "id",
            "name",
        ]


class RoutineExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineExercise
        fields = [
            "id",
            "routine",
            "exercise",
        ]


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            "id",
            "created_on",
        ]
