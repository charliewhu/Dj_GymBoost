from behave import given, when, then
from selenium.webdriver.common.by import By

from workouts.models import WorkoutExerciseSet


## Given there is a Workout
## And there is an Exercise
## And the Workout has WorkoutExercises


@given("the WorkoutExercise has a WorkoutExerciseSet")
def step_impl(context):
    context.workout_exercise_set = WorkoutExerciseSet.objects.create(
        workout_exercise=context.workout_exercise, weight=100, reps=10
    )


@given("I am on the WorkoutExercise page")
def step_impl(context):
    context.browser.get(context.get_url(context.workout_exercise_set))


@when('I click on the "Delete Set" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_exercise_set_btn").click()


@then("the WorkoutExerciseSet will not show on the WorkoutExercise page")
def step_impl(context):
    list_items = context.browser.find_elements(By.ID, "workout_exercise_set_list_item")
    context.test.assertEqual(len(list_items), 0)
