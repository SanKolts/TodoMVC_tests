Feature: mark items as done
  to feel satisfied I need possibility to mark things as done,
  also my team lead will be happy too

  Scenario: mark item as done
    Given the site is opened
    And I have three items in list
    When I click completed button on second item
    Then this task should become completed
    And counter at the bottom should show 2
