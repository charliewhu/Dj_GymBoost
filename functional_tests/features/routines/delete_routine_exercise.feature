Feature: Delete Routine Exercise
    As a User with a Routine with Routine Exercises
    I want to be able to delete Exercises from the Routine
    So that they do not show any more

    Scenario: Delete RoutineExercises from a Routine and remove them from the screen

        Given there is a RoutineExercise
        And I am on the Routine page

        When I click button with id "delete_routine_exercise_btn"

        Then I will see "0" "routine_exercise_list_item" items listed