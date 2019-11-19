Feature: Find cbr.ru with Google, write a thank you note, find and compare warning in en and ru

  Scenario: Search "Центральный банк РФ"
    Given I go to "https://www.google.ru/"
    And I see a searchbox
    When I type "Центральный банк РФ"
    Then I click Google Search

  Scenario: Find cbr.ru among results
    Given Title of the page is "Центральный банк РФ - Поиск в Google"
    When I see "cbr.ru" partial link
    Then I click on the "cbr.ru"

  Scenario: Write Thank You note
    Given Page's title has "Центральный банк Российской Федерации"
    When I press "Интернет-приемная"
    And I open "Написать благодарность" section
    And Enter "случайный текст" into the field
    And Check "Я согласен"
    Then I make a screenshot

  Scenario: Find warning page
    When I press three lines menu
    And I open "О сайте" section
    And I click on link "Предупреждение"
    Then Title of the page is "Предупреждение | Банк России"

  Scenario: Compare warnings in en and ru
    Given I save warning text
    When I click on "EN"
    And I save new warning text
    Then I compare new warning text with the old
    And I save a screenshot