# Created by Nandini at 4/24/2024
Feature: Cart tests
  # Enter feature description here

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Product add in cart icon
    Given Open Target main page
    Then Verify product has shown in chart