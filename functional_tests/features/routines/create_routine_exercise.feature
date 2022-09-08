Feature: Add Routine Exercises
    As a user who has created a Routine
    I want to be able to add Exercises to the Routine
    So that I can use it for a Workout

    Scenario: Add Exercises to a Routine and display them on the Routine screen

        Given there is a Routine with name "FT Routine"
        And there is an Exercise with name "FT Exercise"
        And I am on the Routine page

        When I click button with id "add_routine_exercise_btn"

        Then I will be on the "Exercises" page
        And I will see the Exercises listed
        
        When I click button with id "add_exercise_to_routine_btn"

        Then I will be on the "FT Routine" page
        And I will see element "routine_exercise_list_item"