from behave import given, when, then
from selenium.webdriver.common.by import By


@given("there are Exercises")
def step_impl(context):
    raise NotImplementedError("STEP: Given there are Exercises")


# Given I am on the Exercises page


@when('I click "Delete Exercise"')
def step_impl(context):
    raise NotImplementedError('STEP: When I click "Delete Exercise"')


@then("the Exercise will not show in the list")
def step_impl(context):
    raise NotImplementedError("STEP: Then the Exercise will not show in the list")
