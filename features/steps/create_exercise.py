from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the Exercise page")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))


@when('I fill the form with "{my_new_exercise}"')
def step_impl(context, my_new_exercise):
    context.browser.find_element(By.ID, "id_name").send_keys(my_new_exercise)


@when('click "Create Exercise"')
def step_impl(context):
    context.browser.find_element(By.ID, "exercise_submit_btn")


@then('"My New Exercise" will show on the list')
def step_impl(context):
    raise NotImplementedError('STEP: Then "My New Exercise" will show on the list')
