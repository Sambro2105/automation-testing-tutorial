Feature: Search "Центральный банк РФ" with google.ru

  Scenario: Search "Центральный банк РФ"
    Given I go to "https://www.google.ru/"
    And I see a searchbox
    When I type "Центральный банк РФ"
    And I click Google Search
    Then I see search results