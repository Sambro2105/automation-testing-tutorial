from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from features.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchPageLocator(object):
    # Search Page Locators

    SEARCH_FIELD = (By.NAME, "q")
    SUBMIT_BUTTON = (By.CLASS_NAME, "gNO89b")


class SearchPage(Browser):
    # Search Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def is_there_a_searchbox(self):
        try:
            element_present = EC.visibility_of(self.get_element(*SearchPageLocator.SEARCH_FIELD))
            WebDriverWait(self.driver, 3).until(element_present)
        except TimeoutException:
            return False
        try:
            self.get_element(*SearchPageLocator.SEARCH_FIELD)
        except NoSuchElementException:
            return False
        return True

    def navigate(self, address):
        self.driver.get(address)

    def type_search_request(self, request):
        self.get_element(*SearchPageLocator.SEARCH_FIELD).send_keys(request)

    def click_search(self):
        self.get_element(*SearchPageLocator.SUBMIT_BUTTON).click()
