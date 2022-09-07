from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .forms import RoutineForm
from .models import Routine

# Create your views here.
def routines(request):

    form = RoutineForm()
    routines = Routine.objects.all()
    context = {"title": "Routines", "form": form, "routines": routines}
    return render(request, "routines/routines.html", context)


def routine(request, pk):
    routine = Routine.objects.get(id=pk)
    context = {"title": routine.name}
    return render(request, "routines/routine.html", context)


def routine_create(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save()
            return redirect(routine)
