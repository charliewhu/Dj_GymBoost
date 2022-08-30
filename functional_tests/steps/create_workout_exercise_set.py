from behave import given, when, then
from selenium.webdriver.common.by import By

from exercises.models import Exercise
from workouts.models import WorkoutExercise


## Given there is a Workout


@given("the Workout has a WorkoutExercise")
def step_impl(context):
    context.exercise = Exercise.objects.create(name="test")
    context.workout_exercise = WorkoutExercise.objects.create(
        workout=context.workout, exercise=context.exercise
    )


@given("I am on the WorkoutExercise page")
def step_impl(context):
    context.browser.get(
        context.get_url("workout_exercise", context.workout_exercise.id)
    )
    context.test.assertEqual("Sets")


@when("I fill in the Weight and Reps fields")
def step_impl(context):
    context.browser.find_element(By.ID, "weight_input").send_keys("100")
    context.browser.find_element(By.ID, "reps_input").send_keys("10")


@when('I click on the "Add Set" button')
def step_impl(context):
    context.browser.find_element(By.ID, "set_submit_btn").click()


@then("I will see the Set listed")
def step_impl(context):
    weight_item = context.browser.find_element(By.ID, "weight_item")
    reps_item = context.browser.find_element(By.ID, "reps_item")
    context.test.assertEqual(weight_item.get_attribute("innerHTML"), 100)
    context.test.assertEqual(reps_item.get_attribute("innerHTML"), 10)


@when("I do not fill in the Weight and Reps fields")
def step_impl(context):
    pass


## And I click the "Add Set" button


@then("I will not see any additional Set listed")
def step_impl(context):
    weight_items = context.browser.find_elements(By.ID, "weight_item")
    context.test.assertEqual(
        len(weight_items),
        1,
    )
