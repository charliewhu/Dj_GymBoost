Feature: Create Workout
    As a user on the homepage
    I want to be able to create a new Workout
    So that I can add Exercises/Sets to it later on

    Scenario: Create a Workout and redirect to the Workout

        Given I am on the Home page

        When I click on the Create Workout button

        Then I will see the Workout screen for that Workout