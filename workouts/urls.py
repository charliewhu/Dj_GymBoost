from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("workouts/<int:pk>/", views.workout, name="workout"),
    path("workout_exercises/", views.workout_exercises, name="workout_exercises"),
    path(
        "workout_exercises/<int:pk>/delete/",
        views.delete_workout_exercise,
        name="delete_workout_exercise",
    ),
]
