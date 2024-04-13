# Created by Nandini at 4/11/2024
Feature: Target products search test case


  Scenario: Verfiy product search
    Given Open Target main page
    When Click on search bar

  Scenario: Verify Target circle page
    Given Open Target Circle page
    #When Select Target circle
    Then Verify 6 links present

  Scenario: Verify Target product
    Given Open target main page
    When Search for coffee
    Then Add to cart

    #End Homework 4 tests