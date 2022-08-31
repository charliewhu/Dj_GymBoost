from behave import then
from selenium.webdriver.common.by import By

from exercises.models import Exercise


@then('I am redirected to the "Create Exercise" page')
def step_impl(context):
    context.test.assertEqual("Create Exercise", context.browser.title)


@then("I will be redirected to the Exercise page")
def step_impl(context):
    context.test.assertEqual("Exercises", context.browser.title)


@then('"{new_exercise}" will show on the list')
def step_impl(context, new_exercise):
    exercise = context.browser.find_element(By.ID, "exercise_list_item")
    context.test.assertEqual(exercise.get_attribute("innerHTML"), new_exercise)


@then("I am on the Create Exercise page")
def step_impl(context):
    context.test.assertEqual("Create Exercise", context.browser.title)


@then("no Exercise items are added to the list")
def step_impl(context):
    context.browser.get(context.get_url("exercises"))
    list_items = context.browser.find_elements(By.ID, "exercise_list_item")
    context.test.assertEqual(len(list_items), 1)


@then("I get to the WorkoutExercise page")
def step_impl(context):
    context.test.assertEqual(context.browser.title, "Sets")


@then("I will see the Set listed")
def step_impl(context):
    weight_item = context.browser.find_element(By.ID, "weight_list_item")
    reps_item = context.browser.find_element(By.ID, "reps_list_item")
    context.test.assertEqual(weight_item.get_attribute("innerHTML"), "100.0")
    context.test.assertEqual(reps_item.get_attribute("innerHTML"), "10")


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


@then("I will be on the Exercises page")
def confirm_exercises_page(context):
    context.test.assertEqual(context.browser.title, "Exercises")


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


@then('I will be on the "Exercises" page')
def step_impl(context):
    context.test.assertEqual(context.browser.title, "Exercises")


@then('I will be on "Home" page')
def step_impl(context):
    context.test.assertEqual(context.browser.title, "GymBoost Home")


@then("I can see Workouts listed")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_list")
    list_item = context.browser.find_element(By.ID, "workout_list_item")
    context.test.assertIn("Workout on", list_item.get_attribute("innerHTML"))


@then("I am taken to that Workout page")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_exercise_list")


@then("I will be on the WorkoutExercise page")
def step_impl(context):
    context.test.assertEqual(context.browser.title, "Sets")
