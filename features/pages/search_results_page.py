from selenium.webdriver.common.by import By
from features.browser import Browser

class SearchResultsPageLocator(object):
    # Search Results Page Locators

    TITLE_TEXT = "Центральный банк РФ - Поиск в Google"


class SearchResultsPage(Browser):
    # Search Results Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def find_search_result(self, search_result):
        return self.get_element(By.LINK_TEXT, search_result)