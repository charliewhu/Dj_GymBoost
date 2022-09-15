Feature: Add Routine to Workout
    As a user who has created a Routine with Exercises
    I want to be able to add those Exercises to a new Workout
    So that I don't have to pick them from a list

    Scenario: Add RoutineExercises to Workout and display them as WorkoutExercises

        Given there is a RoutineExercise
        And I am on the Routine page

        When I click button with id "add_routine_to_workout_btn"

        Then I will be on the "Workout" page
        And I will see element "workout_exercise_list_item"

    Scenario: Add RoutineExercises to Workout from Routine List and display them as WorkoutExercises

        Given there is a RoutineExercise
        And I am on the Routines page

        When I click button with id "add_routine_to_workout_btn"

        Then I will be on the "Workout" page
        And I will see element "workout_exercise_list_item"