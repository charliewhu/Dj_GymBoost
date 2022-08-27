from behave import given, when, then
from selenium.webdriver.common.by import By


@given("Workouts exist")
def step_impl(context):
    raise NotImplementedError("STEP: Given Workouts exist")


@when("I am on the Home page")
def step_impl(context):
    raise NotImplementedError("STEP: When I am on the Home page")


@then("I can see Workouts listed")
def step_impl(context):
    raise NotImplementedError("STEP: Then I can see Workouts listed")


@when("I click on a Workout")
def step_impl(context):
    raise NotImplementedError("STEP: When I click on a Workout")


@then("I am taken to that Workout page")
def step_impl(context):
    raise NotImplementedError("STEP: Then I am taken to that Workout page")
