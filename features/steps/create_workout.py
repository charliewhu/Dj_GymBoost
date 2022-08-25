from behave import given, when, then


@given("I am on the homepage")
def step_impl(context):
    title = context.browser.title
    context.test.assertIn("GymBoost Home", title)


@when("I click on the Create Workout button")
def step_impl(context):
    raise NotImplementedError()


@then("I will create a Workout")
def step_impl(context):
    raise NotImplementedError()


@then("I will see the Workout screen for that Workout")
def step_impl(context):
    raise NotImplementedError()
