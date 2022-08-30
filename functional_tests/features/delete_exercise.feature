Feature: Delete Exercises
    As a user who has Exercises
    I want to be able to delete Exercises
    So that I cannot use them later on

    Scenario: Delete Exercises and do not show them in the list

        Given there are Exercises
        And I am on the Exercises page

        When I click "Delete Exercise"

        Then the Exercise will not show in the list
