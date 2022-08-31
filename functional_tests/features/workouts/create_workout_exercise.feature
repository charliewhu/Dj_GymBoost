Feature: Add Workout Exercises
    As a user who has created a Workout
    I want to be able to add Exercises to the Workout
    So that I can add Sets to it later on

    Scenario: Add Exercises to a Workout and display them on the Workout screen

        Given there is a Workout
        And there is an Exercise
        And I am on the Workout page

        When I click button with id "add_workout_exercise_btn"

        Then I will be on the Exercises page
        And I will see the Exercises listed
        
        When I click button with id "add_exercise_to_workout_btn"

        Then it will show the exercise on my Workout