Feature: Parameterizing tests in Pytest BDD

  Scenario: Check varieties of fruit
    Given there are 3 varieties of fruits
    When we add a same variety of fruit
    Then there is same count of varieties
    But if we add a different variety of fruit
    Then the count of varieties increases to 4
