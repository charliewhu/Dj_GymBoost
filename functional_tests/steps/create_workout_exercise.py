from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise
from workouts.models import Workout


@given("there is a Workout")
def create_workout(context):
    context.workout = Workout.objects.create()


@given("there is an Exercise")
def step_impl(context):
    context.exercise = Exercise.objects.create(name="test exercise")


@given("I am on the Workout page")
def step_impl(context):
    context.browser.get(context.get_url(context.workout))


@when("I click on the Add Exercise button")
def click_add_workout_exercise_btn(context):

    add_workout_exercise_btn = context.browser.find_element(
        By.ID, "add_workout_exercise_btn"
    )
    add_workout_exercise_btn.click()


@then("I will be on the Exercises page")
def confirm_exercises_page(context):
    context.test.assertEqual(context.browser.title, "Exercises")


@then("I will see the Exercises listed")
def step_impl(context):
    context.exercise_list_items = context.browser.find_elements(
        By.ID, "exercise_list_item"
    )
    context.test.assertEqual(len(context.exercise_list_items), 1)


@when("I click Add on an Exercise")
def click_add_exercise_to_workout(context):
    add_exercise_to_workout_btns = context.browser.find_elements(
        By.ID, "add_exercise_to_workout_btn"
    )
    add_exercise_to_workout_btns[0].click()


@then("it will show the exercise on my Workout")
def confirm_exercise_in_workout(context):
    context.test.assertIn("Workout", context.browser.title)
    workout_exercise_list_item = context.browser.find_element(
        By.ID, "workout_exercise_list_item"
    )
    context.test.assertIn(
        context.exercise.name, workout_exercise_list_item.get_attribute("innerHTML")
    )