from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I am on the homepage")
def confirm_homepage(context):
    title = context.browser.title
    context.test.assertIn("GymBoost Home", title)


@when("I click on the Create Workout button")
def click_create_workout_btn(context):
    create_workout_btn = context.browser.find_element(By.ID, "create_workout_btn")
    create_workout_btn.click()


@then("I will see the Workout screen for that Workout")
def confirm_workout_page(context):
    title = context.browser.title
    context.test.assertIn("Workout", title)
    list = context.browser.find_element(By.ID, "workout_exercise_list")
