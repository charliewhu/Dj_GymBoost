from behave import given, when, then
from selenium.webdriver.common.by import By


## Given I am on the Home page


@when('I click "Exercises" in the Header')
def step_impl(context):
    context.browser.find_element(By.ID, "nav_exercises").click()


@then('I will be on the "Exercises" page')
def step_impl(context):
    context.test.assertEqual(context.browser.title, "Exercises")


@given("I am on the Exercises page")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))
    context.test.assertEqual(context.browser.title, "Exercises")


@when('I click "Home" in the Header')
def step_impl(context):
    context.browser.find_element(By.ID, "nav_home").click()


@then('I will be on "Home" page')
def step_impl(context):
    context.test.assertEqual(context.browser.title, "GymBoost Home")
