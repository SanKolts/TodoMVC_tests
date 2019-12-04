Feature: changing todo item
  sometimes your goals change,
  so you need to be able to change them in the list

  @wip
  Scenario: changing todo item
    Given the site is opened
    And i have three items in list
    When i'm changing the text of the third input to "Спастись от злой кошки"
    Then counter at the bottom should shows 3
    And the 3 item in list should be "Спастись от злой кошки"