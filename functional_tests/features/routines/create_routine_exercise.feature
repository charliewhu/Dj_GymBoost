Feature: Add Routine Exercises
    As a user who has created a Routine
    I want to be able to add Exercises to the Routine
    So that I can use it for a Workout

    Scenario: Add Exercises to a Routine and display them on the Routine screen

        Given there is a Routine
        And there is an Exercise
        And I am on the Routine page

        When I click button with id "add_routine_exercise_btn"

        Then I will be on the "Exercises" page
        And I will see the Exercises listed
        
        When I click button with id "add_exercise_to_routine_btn"

        Then it will show the Exercise on my Routine