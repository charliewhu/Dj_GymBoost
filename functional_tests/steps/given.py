from behave import given

from workouts.models import Workout, WorkoutExercise, WorkoutExerciseSet
from exercises.models import Exercise


## Object creation


@given("there is an Exercise")
def step_impl(context):
    Exercise.objects.create(name="test exercise")


@given("there is a Workout")
def create_workout(context):
    Workout.objects.create()


@given("the Workout has a WorkoutExercise")
def step_impl(context):
    workout = Workout.objects.first()
    exercise = Exercise.objects.first()
    WorkoutExercise.objects.create(workout=workout, exercise=exercise)


@given("the WorkoutExercise has a WorkoutExerciseSet")
def step_impl(context):
    workout_exercise = WorkoutExercise.objects.first()
    WorkoutExerciseSet.objects.create(
        workout_exercise=workout_exercise, weight=100, reps=10
    )


## Page navigation


@given("I am on the Home page")
def confirm_homepage(context):
    context.browser.get(context.get_url("/"))
    title = context.browser.title
    context.test.assertIn("GymBoost Home", title)


@given("I am on the Exercises page")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))
    context.test.assertEqual(context.browser.title, "Exercises")


@given("I am on the Workout page")
def step_impl(context):
    workout = Workout.objects.first()
    context.browser.get(context.get_url(workout))


@given("I am on the WorkoutExercise page")
def step_impl(context):
    workout_exercise = WorkoutExercise.objects.first()
    context.browser.get(context.get_url(workout_exercise))


@given("I am on the Create Exercise page")
def navigate_to_create_exercise_page(context):
    context.browser.get(context.get_url("exercise_create"))
    context.test.assertEqual("Create Exercise", context.browser.title)