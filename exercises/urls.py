from django.urls import path
from . import views

urlpatterns = [
    path("", views.exercises, name="exercises"),
    path("create/", views.exercise_create, name="exercise_create"),
    path("<int:pk>/delete/", views.exercise_delete, name="exercise_delete"),
]
