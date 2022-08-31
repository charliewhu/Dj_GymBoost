Feature: Create Exercise
    As a user on the homepage
    I want to be able to create a new Exercise
    So that I can use it in Workouts

    Scenario: Create an Exercise

        Given I am on the Exercises page

        When I click url with id "url_exercise_create"

        Then I am redirected to the "Create Exercise" page


        When I fill the form with "My New Exercise"
        And I click button with id "exercise_submit_btn"

        Then I will be redirected to the Exercise page 
        And "My New Exercise" will show on the list

        Given I am on the Create Exercise page

        When I do not fill the form
        And I click button with id "exercise_submit_btn"

        Then I am on the Create Exercise page
        And no Exercise items are added to the list
        