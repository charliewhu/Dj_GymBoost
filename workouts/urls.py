from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("workouts/", views.workouts, name="workouts"),
    path("workouts/<int:pk>/", views.workout, name="workout"),
    path("workouts/<int:pk>/delete/", views.workout_delete, name="workout_delete"),
    path(
        "workout_exercises/create/",
        views.workout_exercise_create,
        name="workout_exercise_create",
    ),
    path(
        "workout_exercises/<int:pk>/delete/",
        views.delete_workout_exercise,
        name="delete_workout_exercise",
    ),
    path(
        "workout_exercise/<int:pk>/sets/",
        views.workout_exercise,
        name="workout_exercise",
    ),
    path(
        "workout_exercise_sets/create/",
        views.workout_exercise_set_create,
        name="workout_exercise_set_create",
    ),
    path(
        "workout_exercise_sets/<int:pk>/delete/",
        views.workout_exercise_set_delete,
        name="workout_exercise_set_delete",
    ),
]
