from behave import given, when, then
from selenium.webdriver.common.by import By


from workouts.models import Workout


## Given there is a Workout

## And I am on the Home page


@then("I can see Workouts listed")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_list")
    list_item = context.browser.find_element(By.ID, "workout_list_item")
    context.test.assertIn("Workout on", list_item.get_attribute("innerHTML"))


@when("I click on a Workout")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_list_item").click()


@then("I am taken to that Workout page")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_exercise_list")
