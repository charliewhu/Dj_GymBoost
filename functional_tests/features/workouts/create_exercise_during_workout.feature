Feature: Add Workout Exercises
    As a user who has created a Workout
    I want to be able to add Exercises during the Workout
    So that I can add add it to the Workout later on

    Scenario: Add Exercises during a Workout and be able to add them to the Workout

        Given there is a Workout
        And I am on the Workout page

        When I click button with id "add_workout_exercise_btn"
        
        Then I will be on the "Exercises" page

        When I click button with id "url_exercise_create"

        Then I will be on the "Create Exercise" page

        When I fill the form with "My New Exercise"
        And I click button with id "exercise_submit_btn"

        Then I will be on the "Exercises" page
        And I will see "My New Exercise" on the page
        
        When I click button with id "add_exercise_to_workout_btn"

        Then I will see "1" "workout_exercise_list_item" items listed