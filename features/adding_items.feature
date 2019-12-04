Feature: adding new to_do line to list
  To know what to do next
  I would like to add new line to my to_do list


  Scenario: adding new todo in list
     Given the site is opened
      When i add text in input
    And press enter
    Then i should see this text in list
    And right counter at the bottom

    Scenario: 
