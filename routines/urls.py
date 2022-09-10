from django.urls import path
from . import views

urlpatterns = [
    path("", views.routines, name="routines"),
    path("<int:pk>/", views.routine, name="routine"),
    path("create/", views.routine_create, name="routine_create"),
    path(
        "exercises/create/",
        views.routine_exercise_create,
        name="routine_exercise_create",
    ),
    path(
        "<int:pk>/workout/create/",
        views.routine_workout_create,
        name="routine_workout_create",
    ),
]
