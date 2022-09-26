from rest_framework import serializers

from exercises.models import Exercise
from routines.models import Routine, RoutineExercise


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
