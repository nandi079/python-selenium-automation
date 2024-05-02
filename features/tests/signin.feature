# Created by Nandini at 4/25/2024
Feature: Click on signin button
  # Enter feature description here

  Scenario: User can click on signin button
    Given Open Target main page
    Then Click on Target Signin button
    Then Click on Signin button on right side navigation
    Then Verify Signin page opened
    Then Input field nandinisarkar079@gmail.com is entered
    Then Input password field Monday123 is entered
    Then Click on submit button
    Then Verify Username123 is logged in target page



  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    Then Click on Target Signin button
    Then Click on Signin button on right side navigation
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window
    And switch back to original















