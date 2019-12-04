Feature: changing todo item
  sometimes your goals change,
  so you need to be able to change them in the list

  Scenario: changing todo item
    Given the site is opened
    And I have three items in list
    When I change the text of the third input to "Спастись от злой кошки"
    Then counter at the bottom should show 3
    And the 3 item in the list should be "Спастись от злой кошки"