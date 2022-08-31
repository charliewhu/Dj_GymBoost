Feature: Delete Workout Exercise Sets
    As a User with a Workout with a WorkoutExercise with a WorkoutExerciseSet
    I want to be able to delete WorkoutExerciseSets from the WorkoutExercise
    So that they do not show any more

    Scenario: Delete WorkoutExerciseSets from a WorkoutExercise and remove them from the screen

        Given there is a Workout
        And there is an Exercise
        And the Workout has WorkoutExercises
        And the WorkoutExercise has a WorkoutExerciseSet
        And I am on the WorkoutExercise page

        When I click on the "Delete Set" button

        Then the WorkoutExerciseSet will not show on the WorkoutExercise page