from selenium.webdriver.common.by import By

from features.browser import Browser


class CbeWarningPageLocator(object):
    # Cbr warning Page Locators
    WARNING_TEXT_ID = 'content'


class CbrWarningPage(Browser):
    # Cbr warning Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def click_by_link_text(self, link_text):
        self.get_element(By.LINK_TEXT, link_text).click()

    def get_text_from(self):
        return self.get_element(By.ID, CbeWarningPageLocator.WARNING_TEXT_ID).text

    def click_by_text(self, str):
        self.get_element(By.XPATH, f"//*[contains(text(), '{str}')]" ).click()

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)
