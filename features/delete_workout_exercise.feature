Feature: Delete Workout Exercises
    As a User with a workout with workout Exercises
    I want to be able to delete Exercises from the Workout
    So that they do not show any more

    Scenario: Delete WorkoutExercises from a Workout and remove them from the screen

        Given I am on the Workout page
        And the Workout has WorkoutExercises

        When I click on the "Delete Exercise" button

        Then the WorkoutExercise will not show on the Workout page
        And the WorkoutExercise will be deleted from the database