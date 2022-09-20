Feature: Create Exercise during Routine
    As a user who has created a Routine
    I want to be able to add Exercises during the Routine
    So that I can add add it to the Routine later on

    Scenario: Add Exercises during a Routine and be able to add them to the Routine

        Given there is a Routine
        And I am on the Routine page

        When I click button with id "add_routine_exercise_btn"
        
        Then I will be on the "Exercises" page

        When I click button with id "url_exercise_create"

        Then I will be on the "Create Exercise" page

        When I fill the form with "My New Exercise"
        And I click button with id "exercise_submit_btn"

        Then I will be on the "Exercises" page
        And I will see "My New Exercise" on the page
        
        When I click button with id "add_exercise_to_routine_btn"

        Then I will see "1" "routine_exercise_list_item" items listed