from django.shortcuts import render
from .forms import RoutineForm

# Create your views here.
def routines(request):

    form = RoutineForm()

    context = {"title": "Routines", "form": form}
    return render(request, "routines/routines.html", context)


def routine_create(request):
    pass
