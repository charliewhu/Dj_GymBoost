Feature: Add Workout Exercise Set
    As a user who has created a Workout with Exercises
    I want to be able to add Sets to the WorkoutExercise
    So that I can record my sets

    Scenario: Add Sets to a WorkoutExercise and display them on the WorkoutExercise screen

        Given there is a Workout
        And there is an Exercise
        And the Workout has a WorkoutExercise
        And I am on the Workout page
        
        When I click on the WorkoutExercise
        Then I get to the WorkoutExercise page

        When I fill in the Weight and Reps fields
        And I click on the "Add Set" button

        Then I will see the Set listed
        
        When I do not fill in the Weight and Reps fields
        And I click on the "Add Set" button
        Then I will not see any additional Set listed