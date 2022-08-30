from behave import given, when, then
from selenium.webdriver.common.by import By


## Given I am on the Home page


@when('I click "Exercises" in the Header')
def step_impl(context):
    raise NotImplementedError('STEP: When I click "Exercises" in the Header')


@then('I will be on the "Exercises" page')
def step_impl(context):
    raise NotImplementedError('STEP: Then I will be on the "Exercises" page')
