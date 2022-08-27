from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise
from features.steps.add_workout_exercise import (
    click_add_exercise_to_workout,
    click_add_workout_exercise_btn,
    confirm_exercises_page,
)

from workouts.models import Workout


@given("I am on the Workout page")
def step_impl(context):
    Workout.objects.create()


@given("the Workout has WorkoutExercises")
def add_exercise_to_workout(context):
    context.exercise = Exercise.objects.create(name="test exercise")
    click_add_workout_exercise_btn(context)
    confirm_exercises_page(context)
    click_add_exercise_to_workout(context)


@when('I click on the "Delete Exercise" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_exercise_btn").click()


@then("the WorkoutExercise will not show on the Workout page")
def step_impl(context):
    workout_exercise_list_items = context.browser.find_elements(
        By.ID, "workout_exercise_list_item"
    )
    context.test.assertEqual(workout_exercise_list_items, [])
