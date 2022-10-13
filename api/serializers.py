from rest_framework import serializers

from exercises.models import Exercise
from routines.models import Routine, RoutineExercise
from workouts.models import Workout, WorkoutExercise, WorkoutExerciseSet


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
        fields = ["id", "routine", "exercise", "name"]

        read_only_fields = [
            "name",
        ]

    name = serializers.StringRelatedField(source="exercise")


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            "id",
            "created_on",
            "routine",
            "name",
        ]

        read_only_fields = [
            "name",
        ]

    name = serializers.StringRelatedField(source="routine")


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = [
            "id",
            "workout",
            "exercise",
            "name",
            "set_count",
        ]

        read_only_fields = [
            "name",
        ]

    name = serializers.StringRelatedField(source="exercise")

    def get_set_count(self, instance):
        instance.get_set_count()


class WorkoutExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExerciseSet
        fields = [
            "id",
            "workout_exercise",
            "weight",
            "reps",
            "rir",
        ]
