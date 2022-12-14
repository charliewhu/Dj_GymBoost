from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .forms import RoutineForm
from .models import Routine, RoutineExercise
from exercises.models import Exercise

# Create your views here.
def routines(request):

    form = RoutineForm()
    routines = Routine.objects.all()
    context = {"title": "Routines", "form": form, "routines": routines}
    return render(request, "routines/routines.html", context)


def routine(request, pk):
    routine = Routine.objects.get(id=pk)
    routine_exercises = RoutineExercise.objects.filter(routine=routine)
    context = {
        "title": routine.name,
        "routine": routine,
        "routine_exercises": routine_exercises,
    }
    return render(request, "routines/routine.html", context)


def routine_create(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save()
            return redirect(routine)


def routine_delete(request, pk):
    if request.method == "POST":
        Routine.objects.get(id=pk).delete()
        return redirect(reverse("routines"))


def routine_exercise_create(request):
    if request.method == "POST":
        routine_id = request.POST.get("routine_id")
        exercise_id = request.POST.get("exercise_id")
        routine = Routine.objects.get(id=routine_id)
        exercise = Exercise.objects.get(id=exercise_id)
        RoutineExercise.objects.create(routine=routine, exercise=exercise)
        return redirect(routine)


def routine_exercise_delete(request, pk):
    if request.method == "POST":
        routine_exercise = RoutineExercise.objects.get(id=pk)
        routine_exercise.delete()
        return redirect(routine_exercise.routine)


def routine_workout_create(request, pk):
    routine = Routine.objects.get(id=pk)
    workout = routine.create_workout()
    return redirect(workout)
