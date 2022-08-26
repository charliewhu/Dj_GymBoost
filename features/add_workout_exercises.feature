Feature: Add Workout Exercises
    As a user who has created a Workout
    I want to be able to add Exercises to the Workout
    So that I can add Sets to it later on

    Scenario: Add Exercises to a Workout and display them on the Workout screen

        Given I have created a Workout
        And I am on the page for that Workout

        When I click on the Add Exercise button

        Then I will see the Exercises listed
        
        When I click Add on an Exercise

        Then it will add the exercise to my Workout
        And show the exercise on my Workout screen