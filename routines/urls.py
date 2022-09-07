from django.urls import path
from . import views

urlpatterns = [
    path("", views.routines, name="routines"),
    path("<int:pk>/", views.routine, name="routine"),
    path("create/", views.routine_create, name="routine_create"),
]
