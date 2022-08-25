from behave import given, when, then
from selenium.webdriver.common.by import By

from features.helpers import get_inner_html


@given("I am on the homepage")
def step_impl(context):
    title = context.browser.title
    context.test.assertIn("GymBoost Home", title)


@when("I click on the Create Workout button")
def step_impl(context):
    create_workout_btn = context.browser.find_element(By.ID, "create_workout_btn")
    create_workout_btn.click()


@then("I will see the Workout screen for that Workout")
def step_impl(context):
    title = context.browser.title
    context.test.assertIn("Workout", title)
    list = context.browser.find_element(By.ID, "workout_exercise_list")
