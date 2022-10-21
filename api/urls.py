from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
    path("routines/<int:pk>/workout/", views.routine_workout, name="routine_workout"),
    path(
        "workoutexercises/<int:pk>/delete_sets/",
        views.workout_exercise_delete_related_sets,
        name="workout_exercise_delete_related_sets",
    ),
]

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
router.register(
    "workoutexercisesets",
    views.WorkoutExerciseSetViewSet,
    basename="workoutexercisesets",
)

urlpatterns += router.urls
