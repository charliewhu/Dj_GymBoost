from django.shortcuts import render
from .forms import ExerciseForm
from .models import Exercise

# Create your views here.
def exercises(request):
    workout_id = request.GET.get("workout_id")
    form = ExerciseForm()
    context = {
        "exercises": Exercise.objects.all(),
        "workout_id": workout_id,
        "form": form,
    }
    return render(request, "exercises/exercises.html", context)
