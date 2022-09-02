from datetime import date

from behave import then
from selenium.webdriver.common.by import By

from exercises.models import Exercise
from workouts.tests.factory import WorkoutExerciseSetFactory


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


@then("I will see the Set listed")
def step_impl(context):
    weight_item = context.browser.find_element(By.ID, "weight_list_item")
    reps_item = context.browser.find_element(By.ID, "reps_list_item")
    context.test.assertEqual(weight_item.get_attribute("innerHTML"), "90.0")
    context.test.assertEqual(reps_item.get_attribute("innerHTML"), "8")


@then("I will not see any additional Set listed")
def step_impl(context):
    weight_list_item = context.browser.find_elements(By.ID, "weight_list_item")
    reps_list_item = context.browser.find_elements(By.ID, "reps_list_item")
    context.test.assertEqual(
        len(weight_list_item),
        1,
    )
    context.test.assertEqual(
        len(reps_list_item),
        1,
    )


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


@then("the WorkoutExerciseSet will not show on the WorkoutExercise page")
def step_impl(context):
    list_items = context.browser.find_elements(By.ID, "workout_exercise_set_list_item")
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


@then("I will still only see 1 WorkoutExerciseSet listed")
def step_impl(context):
    context.test.assertEqual(
        len(context.browser.find_elements(By.ID, "weight_list_item")), 1
    )


@then("I will see the updated WorkoutExerciseSet listed")
def step_impl(context):
    context.test.assertIn(
        "90.0",
        context.browser.find_element(By.ID, "weight_list_item").get_attribute(
            "innerHTML"
        ),
    )
    context.test.assertIn(
        "8",
        context.browser.find_element(By.ID, "reps_list_item").get_attribute(
            "innerHTML"
        ),
    )


@then('I will see "Workout on" todays date')
def step_impl(context):
    workout_date = date.today().strftime("%d-%b-%y")
    text = f"Workout on {workout_date}"
    context.browser.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
