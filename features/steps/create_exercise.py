from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the Exercise page")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))


@when('I fill the form with "{new_exercise}"')
def step_impl(context, new_exercise):
    context.browser.find_element(By.ID, "id_name").send_keys(new_exercise)


@when('click "Create Exercise"')
def step_impl(context):
    context.browser.find_element(By.ID, "exercise_submit_btn").click()


@then('"{new_exercise}" will show on the list')
def step_impl(context, new_exercise):
    exercise = context.browser.find_element(By.ID, "exercise_list_item")
    context.test.assertEqual(exercise.get_attribute("innerHTML"), new_exercise)


@when("I do not fill the form")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))


## And I click create exercise


@then("no items are added to the list")
def step_impl(context):
    list_items = context.browser.find_elements(By.ID, "exercise_list_item")
    context.test.assertEqual(len(list_items), 1)
