# Created by Nandini at 5/5/2024
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select help topic Promotions & Coupons
    Then Verify help Current promotions page opened



Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened




Scenario: User can select Help topic Target GiftCard
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Gift Cards
    Then Verify help Target GiftCard balance page opened
