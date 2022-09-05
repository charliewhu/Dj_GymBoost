from behave import when
from selenium.webdriver.common.by import By

## Exercises


@when('I click url with id "{url_id}"')
def step_impl(context, url_id):
    context.browser.find_element(By.ID, url_id).click()


@when('I fill the form with "{new_exercise}"')
def step_impl(context, new_exercise):
    context.browser.find_element(By.ID, "id_name").send_keys(new_exercise)


@when('I click button with id "{btn_id}"')
def step_impl(context, btn_id):
    context.browser.find_element(By.ID, btn_id).click()


@when("I do not fill the form")
def step_impl(context):
    pass


@when('I fill the "{input_id}" field with "{input_value}"')
def step_impl(context, input_id, input_value):
    context.browser.find_element(By.ID, input_id).clear()
    context.browser.find_element(By.ID, input_id).send_keys(input_value)


@when("I do not fill in the Weight and Reps fields")
def step_impl(context):
    pass
