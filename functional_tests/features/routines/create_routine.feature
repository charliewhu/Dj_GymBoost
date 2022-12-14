Feature: Create Routine
    As a user 
    I want to be able to create a new Routine
    So that I can add Exercises/Sets to it later on

    Scenario: Create a Routine and redirect to the Routine

        Given there is an Exercise
        And I am on the Routines page

        When I fill the "id_name" field with "Test Routine"
        And I click button with id "create_routine_btn"

        Then I will be on the "Test Routine" page
    
    Scenario: Show created Routine in the list

        Given there is a Routine with name "FT Routine"
        And there is an Exercise with name "FT Exercise"
        And I am on the Routines page

        Then I will see element "routine_list"
        And I will see "1" "routine_list_item" items listed