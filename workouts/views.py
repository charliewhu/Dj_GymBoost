from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from workouts.models import Workout, WorkoutExercise, WorkoutExerciseSet
from exercises.models import Exercise

# Create your views here.
def home(request):

    workouts = Workout.objects.all()
    context = {
        "workouts": workouts,
    }
    return render(request, "home.html", context)


def workouts(request):
    if request.method == "POST":
        workout = Workout.objects.create()
        return redirect(workout)


def workout(request, pk):

    workout = Workout.objects.get(id=pk)
    workout_exercises = workout.exercises.all()
    context = {
        "workout": workout,
        "workout_exercises": workout_exercises,
    }
    return render(request, "workouts/workout.html", context)


def workout_delete(request, pk):
    if request.method == "POST":
        Workout.objects.get(id=pk).delete()
        return redirect(home)


def workout_exercise_create(request):
    if request.method == "POST":
        workout_id = request.POST["workout_id"]
        exercise_id = request.POST["exercise_id"]
        workout = Workout.objects.get(id=workout_id)
        exercise = Exercise.objects.get(id=exercise_id)
        WorkoutExercise.objects.create(workout=workout, exercise=exercise)
        return redirect(workout)


def delete_workout_exercise(request, pk):
    workout_exercise = WorkoutExercise.objects.get(id=pk)
    workout = workout_exercise.workout
    if request.method == "POST":
        workout_exercise.delete()
        return redirect(workout)


def workout_exercise(request, pk):
    workout_exercise = WorkoutExercise.objects.get(id=pk)
    sets = workout_exercise.sets.all()
    context = {
        "workout_exercise": workout_exercise,
        "sets": sets,
    }
    return render(request, "workouts/workout_exercise.html", context)


def workout_exercise_set_create(request):
    if request.method == "POST":
        workout_exercise_id = request.POST["workout_exercise_id"]
        workout_exercise = WorkoutExercise.objects.get(id=workout_exercise_id)
        WorkoutExerciseSet.objects.create(workout_exercise=workout_exercise)
        return redirect(reverse("workout_exercise", args=[workout_exercise.id]))
