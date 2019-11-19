# Created by Sambro at 18.11.2019
Feature: User searches for cbr.ru
  ''' User opens google.ru, finds 'search' field,
  types 'Центральный банк РФ'
  and presses 'Google Search' '''

  Scenario: User looks for "Центральный банк РФ" with google.ru
    Given: "google.ru" opens
    When: User sees a search field
    Then: User types "Центральный банк РФ" into the search field
    And: User clicks "Google Search"