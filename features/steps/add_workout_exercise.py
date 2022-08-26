from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I have created a Workout")
def step_impl(context):
    raise NotImplementedError("STEP: Given I have created a Workout")


@given("I am on the page for that Workout")
def step_impl(context):
    raise NotImplementedError("STEP: Given I am on the page for that Workout")


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
