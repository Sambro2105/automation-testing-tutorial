from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from features.browser import Browser

class SearchPageLocator(object):
    # Search Page Locators

    SEARCH_FIELD = (By.NAME, "q")
    SUBMIT_BUTTON = (By.CLASS_NAME, "gNO89b")


class SearchPage(Browser):
    # Search Page Actions

    def find_searchbox(self):
        try:
            self.driver.find_element(SearchPageLocator.SEARCH_FIELD[0], SearchPageLocator.SEARCH_FIELD[1])
        except NoSuchElementException:
            return False
        return True

    def navigate(self, address):
        self.driver.get(address)

    def type_search_request(self, request):
        self.driver.find_element(SearchPageLocator.SEARCH_FIELD[0], SearchPageLocator.SEARCH_FIELD[1]).send_keys(request)

    def click_search(self):
        self.driver.find_element(SearchPageLocator.SUBMIT_BUTTON[0], SearchPageLocator.SUBMIT_BUTTON[1]).click()