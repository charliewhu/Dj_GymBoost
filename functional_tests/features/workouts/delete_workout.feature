Feature: Delete Workouts
    As a User with Workouts
    I want to be able to delete Workouts
    So that they do not show any more

    Scenario: Delete Workouts remove them from the screen

        Given there is a workout
        And I am on the Home page

        When I click on the "Delete Workout" button

        Then the Workout will not show on the page