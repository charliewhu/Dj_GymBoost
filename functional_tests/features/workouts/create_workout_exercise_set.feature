Feature: Add Workout Exercise Set
    As a user who has created a Workout with Exercises
    I want to be able to add Sets to the WorkoutExercise
    So that I can record my sets

    Scenario: Add Sets to a WorkoutExercise and display them on the WorkoutExercise screen

        Given there is a Workout
        And there is an Exercise
        And the Workout has a WorkoutExercise
        And I am on the WorkoutExercise page
        
        When I fill the "id_weight" field with "50" 
        And I fill the "id_reps" field with "10"
        And I fill the "id_rir" field with "2"
        And I click button with id "workout_exercise_set_submit_btn"

        Then I will see "1" "workout_exercise_set_list_item" items listed
        And "weight_list_item" has value "50"
        And "reps_list_item" has value "10"
        And "rir_list_item" has value "2"
        
        When I do not fill in the Weight and Reps fields
        And I click button with id "workout_exercise_set_submit_btn"

        Then I will see "1" "workout_exercise_set_list_item" items listed


    Scenario: Add invalid Sets to a WorkoutExercise and do not display them on the WorkoutExercise screen

        Given there is a Workout
        And there is an Exercise
        And the Workout has a WorkoutExercise
        And I am on the WorkoutExercise page
        
        When I fill the "id_reps" field with "-1" 
        And I fill the "id_rir" field with "10"
        And I click button with id "workout_exercise_set_submit_btn"
        
        Then I will see "0" "workout_exercise_set_list_item" items listed