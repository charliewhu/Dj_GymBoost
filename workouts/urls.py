from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("workouts/<int:pk>/", views.workout, name="workout"),
]
