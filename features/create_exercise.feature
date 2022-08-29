Feature: Create Exercise
    As a user on the homepage
    I want to be able to create a new Exercise
    So that I can use it in Workouts

    Scenario: Create an Exercise

        Given I am on the Exercise page

        When I fill the form with "My New Exercise"
        And click "Create Exercise"

        Then "My New Exercise" will show on the list
        