Feature: Delete Routine
    As a User with a Routine
    I want to be able to delete the Routine
    So that they do not show any more

    Scenario: Delete a Routine and remove them from the screen

        Given there is a Routine
        And I am on the Routines page

        When I click button with id "delete_routine_btn"

        Then I will see element "routine_list"
        And I will see "0" "routine_list_item" items listed