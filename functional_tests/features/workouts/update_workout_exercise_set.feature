Feature: Update WorkoutExerciseSet
    As a user with a WorkoutExerciseSet
    I want to be able to edit the set
    So that I can correct mistakes

    Scenario: Update existing WorkoutExerciseSet

        Given there is a WorkoutExerciseSet
        And I am on the WorkoutExercise page

        When I click button with id "workout_exercise_set_update_btn"

        Then the form will fill with the WorkoutExerciseSet info


        When I fill the "id_weight" field with "50" 
        And I fill the "id_reps" field with "10"
        And I fill the "id_rir" field with "2"
        And I click button with id "workout_exercise_set_submit_btn"

        Then I will see "1" "workout_exercise_set_list_item" items listed
        And "weight_list_item" has value "50"
        And "reps_list_item" has value "10"
        And "rir_list_item" has value "2"
