from django.urls import path
from . import views

urlpatterns = [
    path("", views.exercises, name="exercises"),
    path("create/", views.exercise_create, name="exercise_create"),
]
