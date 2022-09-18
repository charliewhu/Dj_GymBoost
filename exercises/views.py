from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ExerciseForm
from .models import Exercise

# Create your views here.
def exercises(request):

    context = {
        "title": "Exercises",
        "exercises": Exercise.objects.all(),
        "workout_id": request.GET.get("workout_id"),
        "routine_id": request.GET.get("routine_id"),
    }

    return render(request, "exercises/exercises.html", context)


def exercise_create(request):

    form = ExerciseForm()

    if request.method == "POST":
        print(request.POST)
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("exercises"))

    try:
        workout_id = request.GET.get("workout_id")
    except:
        workout_id = None

    context = {"title": "Create Exercise", "form": form, "workout_id": workout_id}
    return render(request, "exercises/create.html", context)


def exercise_delete(request, pk):
    if request.method == "POST":
        Exercise.objects.get(id=pk).delete()
        return redirect(reverse("exercises"))
