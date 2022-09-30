from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = []
router = SimpleRouter()
router.register("exercises", views.ExerciseViewSet, basename="exercises")
router.register("routines", views.RoutineViewSet, basename="routines")
router.register(
    "routineexercises", views.RoutineExerciseViewSet, basename="routineexercises"
)
router.register("workouts", views.WorkoutViewSet, basename="workouts")
router.register(
    "workoutexercises", views.WorkoutExerciseViewSet, basename="workoutexercises"
)

urlpatterns += router.urls
