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


@when("I fill in the Weight and Reps fields")
def step_impl(context):
    context.browser.find_element(By.ID, "id_weight").send_keys("100")
    context.browser.find_element(By.ID, "id_reps").send_keys("10")


@when("I do not fill in the Weight and Reps fields")
def step_impl(context):
    pass
