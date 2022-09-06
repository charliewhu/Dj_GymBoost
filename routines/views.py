from django.shortcuts import render

# Create your views here.
def routines(request):
    context = {
        "title": "Routines",
    }
    return render(request, "routines/routines.html", context)
