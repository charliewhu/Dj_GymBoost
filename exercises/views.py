from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ExerciseForm
from .models import Exercise

# Create your views here.
def exercises(request):

    context = {
        "exercises": Exercise.objects.all(),
    }

    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            reverse("exercises")

    context["form"] = ExerciseForm()
    context["workout_id"] = request.GET.get("workout_id")

    return render(request, "exercises/exercises.html", context)
