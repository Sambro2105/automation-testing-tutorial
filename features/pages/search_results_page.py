from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.browser import Browser

class SearchResultsPage(Browser):
    # Search Results Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def is_page_title(self, title):
        return self.get_page_title() == title

    def is_there_a_search_result(self, search_result):
        try:
            self.get_element(By.PARTIAL_LINK_TEXT, search_result)
        except NoSuchElementException:
            return False
        return True

    def click_on_search_result(self, search_result):
        self.get_element(By.PARTIAL_LINK_TEXT, search_result).click()

    def switch(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])