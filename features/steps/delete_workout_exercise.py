from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise
from features.steps.add_workout_exercise import (
    click_add_exercise_to_workout,
    click_add_workout_exercise_btn,
    confirm_exercises_page,
    create_workout,
)


@given("I am on the Workout page")
def step_impl(context):
    create_workout(context)


@given("the Workout has WorkoutExercises")
def add_exercise_to_workout(context):
    context.exercise = Exercise.objects.create(name="test exercise")
    click_add_workout_exercise_btn(context)
    confirm_exercises_page(context)
    click_add_exercise_to_workout(context)


@when('I click on the "Delete Exercise" button')
def step_impl(context):
    raise NotImplementedError('STEP: When I click on the "Delete Exercise" button')


@then("the WorkoutExercise will not show on the Workout page")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the WorkoutExercise will not show on the Workout page"
    )


@then("the WorkoutExercise will be deleted from the database")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the WorkoutExercise will be deleted from the database"
    )
