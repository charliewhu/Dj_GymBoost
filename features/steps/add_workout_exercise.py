from behave import given, when, then
from selenium.webdriver.common.by import By

from features.steps.create_workout import confirm_workout_page, click_create_workout_btn
from exercises.models import Exercise


@given("I have created a Workout")
def create_workout(context):
    click_create_workout_btn(context)
    confirm_workout_page(context)


@given("Exercises exist")
def step_impl(context):
    context.exercise = Exercise.objects.create(name="Test Exercise")


@when("I click on the Add Exercise button")
def click_add_workout_exercise_btn(context):
    add_workout_exercise_btn = context.browser.find_element(
        By.ID, "add_workout_exercise_btn"
    )
    add_workout_exercise_btn.click()


@then("I will be on the Exercises page")
def step_impl(context):
    context.test.assertEqual(context.browser.title, "Exercises")


@then("I will see the Exercises listed")
def step_impl(context):
    context.exercise_list_items = context.browser.find_elements(
        By.ID, "exercise_list_item"
    )
    context.test.assertEqual(len(context.exercise_list_items), 1)


@when("I click Add on an Exercise")
def add_exercise_to_workout(context):
    add_exercise_to_workout_btns = context.browser.find_elements(
        By.ID, "add_exercise_to_workout_btn"
    )
    add_exercise_to_workout_btns[0].click()


@then("it will add the exercise to my Workout")
def step_impl(context):
    context.test.assertIn("Workout", context.browser.title)
    context.workout_exercise_list_item = context.browser.find_elements(
        By.ID, "workout_exercise_list_item"
    )
    context.test.assertEqual(len(context.workout_exercise_list_item), 1)


@then("show the exercise on my Workout screen")
def step_impl(context):
    assert context.workout_exercise_list_item[0] in context.exercise_list_items[0]
