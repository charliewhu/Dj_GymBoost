from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = []
router = SimpleRouter()
router.register("exercises", views.ExerciseViewSet, basename="exercises")

urlpatterns += router.urls
