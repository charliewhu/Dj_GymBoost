Feature: Navigation Header
    As a user
    I want to be able to navigate to certain pages from all other pages
    So that I can navigate without typing URLs

    Scenario: Navigate from all pages

        Given I am on the Home page
        When I click "Exercises" in the Header
        Then I will be on the "Exercises" page

        Given I am on the Exercises page
        When I click "Home" in the Header
        Then I will be on "Home" page