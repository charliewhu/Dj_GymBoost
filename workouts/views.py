from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from workouts.models import Workout, WorkoutExercise
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


def workout_exercises(request, pk):
    pass


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
