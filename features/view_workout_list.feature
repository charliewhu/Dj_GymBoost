Feature: View list of Workouts
    As a user
    I want to be able to see existing Workouts
    So that I can find them from the Home page

    Scenario: View list of Workouts from the Home page

        Given Workouts exist

        When I am on the Home page

        Then I can see Workouts listed

        When I click on a Workout

        Then I am taken to that Workout page