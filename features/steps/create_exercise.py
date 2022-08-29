from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the Create Exercise page")
def navigate_to_create_exercise_page(context):
    context.browser.get(context.get_url("exercise_create"))
    context.test.assertEqual("Create Exercise", context.browser.title)


@when('I fill the form with "{new_exercise}"')
def step_impl(context, new_exercise):
    context.browser.find_element(By.ID, "id_name").send_keys(new_exercise)


@when('I click "Create Exercise"')
def step_impl(context):
    context.browser.find_element(By.ID, "exercise_submit_btn").click()


@then("I will be redirected to the Exercise page")
def step_impl(context):
    context.test.assertEqual("Exercises", context.browser.title)


@then('"{new_exercise}" will show on the list')
def step_impl(context, new_exercise):
    exercise = context.browser.find_element(By.ID, "exercise_list_item")
    context.test.assertEqual(exercise.get_attribute("innerHTML"), new_exercise)


## Given I am on the Create Exercise page


@when("I do not fill the form")
def step_impl(context):
    pass


## And I click create exercise


@then("I am still on the Create Exercise page")
def step_impl(context):
    context.test.assertEqual("Create Exercise", context.browser.title)


@then("no Exercise items are added to the list")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))
    list_items = context.browser.find_elements(By.ID, "exercise_list_item")
    context.test.assertEqual(len(list_items), 1)
