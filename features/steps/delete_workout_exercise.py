from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the Workout page")
def step_impl(context):
    raise NotImplementedError("STEP: Given I am on the Workout page")


@given("the Workout has WorkoutExercises")
def step_impl(context):
    raise NotImplementedError("STEP: Given the Workout has WorkoutExercises")


@when('I click on the "Delete Exercise" button')
def step_impl(context):
    raise NotImplementedError('STEP: When I click on the "Delete Exercise" button')


@then("the WorkoutExercise will not show on the Workout page")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the WorkoutExercise will not show on the Workout page"
    )


@then("the WorkoutExercise will be deleted from the database")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the WorkoutExercise will be deleted from the database"
    )
