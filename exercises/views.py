from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ExerciseForm
from .models import Exercise

# Create your views here.
def exercises(request):

    context = {
        "exercises": Exercise.objects.all(),
        "workout_id": request.GET.get("workout_id"),
    }

    return render(request, "exercises/exercises.html", context)


def exercise_create(request):

    form = ExerciseForm()

    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("exercises"))

    context = {"form": form}
    return render(request, "exercises/create.html", context)


def exercise_delete(request, pk):
    if request.method == "POST":
        return redirect(reverse("exercises"))
