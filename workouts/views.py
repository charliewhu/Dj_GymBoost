from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from .forms import WorkoutExerciseSetForm
from .models import Workout, WorkoutExercise, WorkoutExerciseSet

from exercises.models import Exercise

# Create your views here.
def home(request):

    workouts = Workout.objects.all()
    context = {
        "title": "GymBoost Home",
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
        "title": "Workout",
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
    if request.method == "POST":
        workout_exercise.delete()
        return redirect(workout_exercise.workout)


def workout_exercise(request, pk):
    workout_exercise = WorkoutExercise.objects.get(id=pk)
    sets = WorkoutExerciseSet.objects.filter(workout_exercise=workout_exercise)
    set_ = WorkoutExerciseSet.objects.filter(id=request.GET.get("id")).first() or None
    form = WorkoutExerciseSetForm(instance=set_)

    context = {
        "title": "Workout Exercise",
        "workout_exercise": workout_exercise,
        "sets": sets,
        "workout_exercise_set": set_,
        "form": form,
    }
    return render(request, "workouts/workout_exercise.html", context)


def workout_exercise_set_create(request):

    if request.method == "POST":

        form = WorkoutExerciseSetForm(request.POST)
        if form.is_valid():
            workout_exercise_id = request.POST["workout_exercise_id"]
            workout_exercise = WorkoutExercise.objects.get(id=workout_exercise_id)
            obj = form.save(commit=False)
            obj.workout_exercise = workout_exercise
            obj.save()

            return redirect(reverse("workout_exercise", args=[workout_exercise_id]))


def workout_exercise_set_update(request, pk):
    workout_exercise_set = WorkoutExerciseSet.objects.get(id=pk)
    if request.method == "POST":
        form = WorkoutExerciseSetForm(request.POST, instance=workout_exercise_set)
        if form.is_valid():
            form.save()
            return redirect(workout_exercise_set.workout_exercise)


def workout_exercise_set_delete(request, pk):
    if request.method == "POST":
        workout_exercise_set = WorkoutExerciseSet.objects.get(id=pk)
        workout_exercise_set.delete()
        return redirect(workout_exercise_set.workout_exercise)
