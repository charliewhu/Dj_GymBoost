Feature: Update WorkoutExerciseSet
    As a user with a WorkoutExerciseSet
    I want to be able to edit the set
    So that I can correct mistakes

    Scenario: Update existing WorkoutExerciseSet

        Given there is a WorkoutExerciseSet
        And I am on the WorkoutExercise page

        When I click button with id "workout_exercise_set_update_btn"

        Then the form will fill with the WorkoutExerciseSet info


        When I fill in the Weight and Reps fields
        And I click button with id "workout_exercise_set_submit_btn"

        Then I will see the set listed
