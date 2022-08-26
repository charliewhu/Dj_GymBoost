from django.shortcuts import render

from exercises.models import Exercise

# Create your views here.
def exercises(request):
    context = {"exercises": Exercise.objects.all()}
    return render(request, "exercises/exercises.html", context)
