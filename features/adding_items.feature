Feature: adding new to_do lines to list
      To know what to do next,
      I would like to add new line to my to_do list


  Scenario: adding new todo in list
     Given the site is opened
      When i add "Текст" in input
    And press enter for text input
    Then the 1 item in list should be "Текст"
    And counter at the bottom should shows 1