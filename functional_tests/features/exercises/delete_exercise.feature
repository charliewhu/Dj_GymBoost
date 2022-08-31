Feature: Delete Exercises
    As a user who has Exercises
    I want to be able to delete Exercises
    So that I cannot use them later on

    Scenario: Delete Exercises and do not show them in the list

        Given there is an Exercise
        And I am on the Exercises page

        When I click button with id "exercise_delete_btn"

        Then I will be on the Exercises page
        And the Exercise will not show in the list
