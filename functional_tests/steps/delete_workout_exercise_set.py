from behave import given, when, then
from selenium.webdriver.common.by import By


## Given there is a Workout
## And there is an Exercise
## And the Workout has WorkoutExercises


@given("the WorkoutExercise has a WorkoutExerciseSet")
def step_impl(context):
    raise NotImplementedError("STEP: Given the WorkoutExercise has a Workout")


@given("I am on the WorkoutExercise page")
def step_impl(context):
    raise NotImplementedError("STEP: Given I am on the WorkoutExercise page")


@when('I click on the "Delete Set" button')
def step_impl(context):
    raise NotImplementedError('STEP: When I click on the "Delete Set" button')


@then("the WorkoutExerciseSet will not show on the WorkoutExercise page")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the WorkoutExerciseSet will not show on the WorkoutExercise page"
    )
