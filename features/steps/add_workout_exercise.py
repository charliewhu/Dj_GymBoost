from behave import given, when, then
from selenium.webdriver.common.by import By

from features.steps.create_workout import confirm_workout_page, create_a_workout


@given("I have created a Workout")
def step_impl(context):
    create_a_workout(context)
    confirm_workout_page(context)


@when("I click on the Add Exercise button")
def step_impl(context):
    raise NotImplementedError("STEP: When I click on the Add Exercise button")


@then("I will see the Exercises listed")
def step_impl(context):
    raise NotImplementedError("STEP: Then I will see the Exercises listed")


@when("I click Add on an Exercise")
def step_impl(context):
    raise NotImplementedError("STEP: When I click Add on an Exercise")


@then("it will add the exercise to my Workout")
def step_impl(context):
    raise NotImplementedError("STEP: Then it will add the exercise to my Workout")


@then("show the exercise on my Workout screen")
def step_impl(context):
    raise NotImplementedError("STEP: Then show the exercise on my Workout screen")
