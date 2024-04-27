# Created by Nandini at 4/24/2024
Feature: Cart tests
  # Enter feature description here

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Product add in cart icon
    Given Open Target main page
    When Search for Tazo Passion Herbal Tea
    Then Verify search results are shown for Tazo Passion Herbal Tea
    Then Add item to cart
    #Then Add item to cart
    Then navigate to cart
    Then Verify Tazo Passion Herbal Tea is shown in cart