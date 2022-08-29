from behave import given, when, then
from selenium.webdriver.common.by import By


# Given I am on the Home page


@when('I click on the "Delete Workout" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_btn").click()


@then("the Workout will not show on the page")
def step_impl(context):
    workout_list_items = context.browser.find_elements(By.ID, "workout_list_item")
    context.test.assertEqual(workout_list_items, [])
