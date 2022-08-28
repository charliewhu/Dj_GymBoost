from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise


from workouts.models import Workout, WorkoutExercise


@given("there is a workout")
def step_impl(context):
    context.workout = Workout.objects.create()


@given("the Workout has WorkoutExercises")
def add_exercise_to_workout(context):
    context.exercise = Exercise.objects.create(name="test exercise")
    WorkoutExercise.objects.create(workout=context.workout, exercise=context.exercise)


@given("I am on the Workout page")
def add_exercise_to_workout(context):
    context.browser.get(context.get_url(context.workout))


@when('I click on the "Delete Exercise" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_exercise_btn").click()


@then("the WorkoutExercise will not show on the Workout page")
def step_impl(context):
    workout_exercise_list_items = context.browser.find_elements(
        By.ID, "workout_exercise_list_item"
    )
    context.test.assertEqual(workout_exercise_list_items, [])
