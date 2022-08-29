from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the home page")
def step_impl(context):
    context.browser.get(context.get_url("/"))


@when('I click on the "Delete Workout" button')
def step_impl(context):
    raise NotImplementedError('STEP: When I click on the "Delete Workout" button')


@then("the Workout will not show on the page")
def step_impl(context):
    raise NotImplementedError("STEP: Then the Workout will not show on the page")
