from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise


from workouts.models import Workout, WorkoutExercise


## Given there is a Workout

## Given there is an Exercise


@given("the Workout has WorkoutExercises")
def add_exercise_to_workout(context):
    WorkoutExercise.objects.create(workout=context.workout, exercise=context.exercise)


## And I am on the Workout page


@when('I click on the "Delete Exercise" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_exercise_btn").click()


@then("the WorkoutExercise will not show on the Workout page")
def step_impl(context):
    workout_exercise_list_items = context.browser.find_elements(
        By.ID, "workout_exercise_list_item"
    )
    context.test.assertEqual(workout_exercise_list_items, [])
