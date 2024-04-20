# Created by Nandini at 4/17/2024
Feature: Test case for search Product
  # Enter feature description here

  Scenario: Search product name and image
    Given Open Target start page
    When Searching 'coffee'
    Then Verify Product Title and Image is shown


