Feature: Changing tabs in todo list
  Sometimes I want to filter my todo list

  @wip
  Scenario: Filter only active tasks
    Given the site is opened
    And I have three items in list
    When I click completed button on second item
    And I click "Active" filter button
    Then I sleep
    Then counter at the bottom should show 2
    And I should see 2 items in todolist
    But not one task is not completed
