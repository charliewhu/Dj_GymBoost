from behave import when
from selenium.webdriver.common.by import By


@when('I click "Create New Exercise"')
def step_impl(context):
    context.browser.find_element(By.ID, "url_exercise_create").click()


@when('I click "Submit"')
def step_impl(context):
    context.browser.find_element(By.ID, "exercise_submit_btn").click()


@when('I fill the form with "{new_exercise}"')
def step_impl(context, new_exercise):
    context.browser.find_element(By.ID, "id_name").send_keys(new_exercise)


@when("I do not fill the form")
def step_impl(context):
    pass


@when("I click on the WorkoutExercise")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_exercise_list_item").click()


@when("I fill in the Weight and Reps fields")
def step_impl(context):
    context.browser.find_element(By.ID, "id_weight").send_keys("100")
    context.browser.find_element(By.ID, "id_reps").send_keys("10")


@when('I click on the "Add Set" button')
def step_impl(context):
    context.browser.find_element(By.ID, "set_submit_btn").click()


@when("I do not fill in the Weight and Reps fields")
def step_impl(context):
    pass


@when("I click on the Add Exercise button")
def click_add_workout_exercise_btn(context):

    add_workout_exercise_btn = context.browser.find_element(
        By.ID, "add_workout_exercise_btn"
    )
    add_workout_exercise_btn.click()


@when("I click Add on an Exercise")
def click_add_exercise_to_workout(context):
    add_exercise_to_workout_btns = context.browser.find_elements(
        By.ID, "add_exercise_to_workout_btn"
    )
    add_exercise_to_workout_btns[0].click()


@when("I click on the Create Workout button")
def click_create_workout_btn(context):
    create_workout_btn = context.browser.find_element(By.ID, "create_workout_btn")
    create_workout_btn.click()


@when('I click "Delete Exercise"')
def step_impl(context):
    context.browser.find_element(By.ID, "exercise_delete_btn").click()


@when('I click on the "Delete Set" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_exercise_set_btn").click()


@when('I click on the "Delete Exercise" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_exercise_btn").click()


@when('I click on the "Delete Workout" button')
def step_impl(context):
    context.browser.find_element(By.ID, "delete_workout_btn").click()


@when('I click "Exercises" in the Header')
def step_impl(context):
    context.browser.find_element(By.ID, "nav_exercises").click()


@when('I click "Home" in the Header')
def step_impl(context):
    context.browser.find_element(By.ID, "nav_home").click()


@when("I click on a Workout")
def step_impl(context):
    context.browser.find_element(By.ID, "workout_list_item").click()
