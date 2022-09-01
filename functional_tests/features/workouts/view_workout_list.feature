Feature: View list of Workouts
    As a user
    I want to be able to see existing Workouts
    So that I can find them from the Home page

    Scenario: View list of Workouts from the Home page

        Given there is a Workout

        And I am on the Workouts page

        Then I can see Workouts listed

        When I click url with id "workout_list_item"

        Then I will be on the "Workout" page