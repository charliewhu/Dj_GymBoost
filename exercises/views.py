from django.shortcuts import render

from exercises.models import Exercise

# Create your views here.
def exercises(request):
    workout_id = request.GET.get("workout_id")
    context = {"exercises": Exercise.objects.all(), "workout_id": workout_id}
    return render(request, "exercises/exercises.html", context)
