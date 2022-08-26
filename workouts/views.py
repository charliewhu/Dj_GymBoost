from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from workouts.models import Workout


# Create your views here.
def home(request):
    if request.method == "POST":
        workout = Workout.objects.create()
        return redirect(workout)
    return render(request, "home.html")


def workout(request, pk):
    context = {"workout": Workout.objects.get(id=pk)}
    return render(request, "workouts/workout.html", context)
