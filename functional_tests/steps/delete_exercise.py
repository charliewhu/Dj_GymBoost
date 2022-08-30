from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise


@given("there are Exercises")
def step_impl(context):
    Exercise.objects.create(name="test")


## And I am on the Exercises page


@when('I click "Delete Exercise"')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_exercise_btn").click()


@then("the Exercise will not show in the list")
def step_impl(context):
    list_items = context.browser.find_elements(By.ID, "exercise_list_item")
    context.test.assertEqual(len(list_items), 0)
