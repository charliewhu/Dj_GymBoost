from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from workouts.models import Workout, WorkoutExercise
from exercises.models import Exercise

# Create your views here.
def home(request):
    if request.method == "POST":
        workout = Workout.objects.create()
        return redirect(workout)
    return render(request, "home.html")


def workout(request, pk):
    context = {"workout": Workout.objects.get(id=pk)}
    return render(request, "workouts/workout.html", context)


def workout_exercises(request):
    if request.method == "POST":
        workout_id = request.POST["workout_id"]
        exercise_id = request.POST["exercise_id"]
        workout = Workout.objects.get(id=workout_id)
        exercise = Exercise.objects.get(id=exercise_id)
        WorkoutExercise.objects.create(workout=workout, exercise=exercise)
        return redirect(workout)
