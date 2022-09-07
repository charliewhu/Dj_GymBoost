from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RoutineForm

# Create your views here.
def routines(request):

    form = RoutineForm()

    context = {"title": "Routines", "form": form}
    return render(request, "routines/routines.html", context)


def routine(request):
    pass


def routine_create(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save()
            return redirect(routine)
