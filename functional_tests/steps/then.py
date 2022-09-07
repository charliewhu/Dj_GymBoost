from datetime import date

from behave import then
from selenium.webdriver.common.by import By

from exercises.models import Exercise
from functional_tests.helpers import get_by_text
from workouts.tests.factory import WorkoutExerciseSetFactory


@then('I will see element "{element_id}"')
def step_impl(context, element_id):
    exercise = context.browser.find_element(By.ID, element_id)


@then('"{new_exercise}" will show on the list')
def step_impl(context, new_exercise):
    exercise = context.browser.find_element(By.ID, "exercise_list_item")
    context.test.assertEqual(exercise.get_attribute("innerHTML"), new_exercise)


@then('I will be on the "{page_title}" page')
def step_impl(context, page_title):
    context.test.assertEqual(page_title, context.browser.title)


@then("no Exercise items are added to the list")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))
    list_items = context.browser.find_elements(By.ID, "exercise_list_item")
    context.test.assertEqual(len(list_items), 1)


@then('"{item_id}" has value "{item_value}"')
def step_impl(context, item_id, item_value):
    item = context.browser.find_element(By.ID, item_id)
    context.test.assertEqual(item.get_attribute("innerHTML"), item_value)


@then('I will see "{item_count}" "{item_id}" items listed')
def step_impl(context, item_count, item_id):
    items = context.browser.find_elements(By.ID, item_id)
    context.test.assertEqual(
        len(items),
        int(item_count),
    )


@then('I will see "{item_id}"')
def step_impl(context, item_id):
    context.browser.find_element(By.ID, item_id)


@then("I will see the Exercises listed")
def step_impl(context):
    context.exercise_list_items = context.browser.find_elements(
        By.ID, "exercise_list_item"
    )
    context.test.assertEqual(len(context.exercise_list_items), 1)


@then("it will show the exercise on my Workout")
def confirm_exercise_in_workout(context):
    context.test.assertIn("Workout", context.browser.title)
    workout_exercise_list_item = context.browser.find_element(
        By.ID, "workout_exercise_list_item"
    )

    exercise = Exercise.objects.first()
    context.test.assertIn(
        exercise.name, workout_exercise_list_item.get_attribute("innerHTML")
    )


@then("I will see the Workout screen for that Workout")
def confirm_workout_page(context):
    title = context.browser.title
    context.test.assertIn("Workout", title)
    list = context.browser.find_element(By.ID, "workout_exercise_list")


@then("the Exercise will not show in the list")
def step_impl(context):
    list_items = context.browser.find_elements(By.ID, "exercise_list_item")
    print(list_items)
    context.test.assertEqual(len(list_items), 0)


@then("the WorkoutExercise will not show on the Workout page")
def step_impl(context):
    workout_exercise_list_items = context.browser.find_elements(
        By.ID, "workout_exercise_list_item"
    )
    context.test.assertEqual(workout_exercise_list_items, [])


@then("the Workout will not show on the page")
def step_impl(context):
    workout_list_items = context.browser.find_elements(By.ID, "workout_list_item")
    context.test.assertEqual(workout_list_items, [])


@then("I can see Workouts listed")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_list")
    list_item = context.browser.find_element(By.ID, "workout_list_item")
    context.test.assertIn("Workout on", list_item.get_attribute("innerHTML"))


@then("the form will fill with the WorkoutExerciseSet info")
def step_impl(context):
    context.test.assertIn(
        str(WorkoutExerciseSetFactory().weight),
        context.browser.find_element(By.ID, "id_weight").get_attribute("value"),
    )
    context.test.assertIn(
        str(WorkoutExerciseSetFactory().reps),
        context.browser.find_element(By.ID, "id_reps").get_attribute("value"),
    )


@then('I will see "Workout on" todays date')
def step_impl(context):
    workout_date = date.today().strftime("%d-%b-%y")
    text = f"Workout on {workout_date}"
    get_by_text(context, text)
