import os
from selenium.webdriver.common.by import By
from features.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CbePageLocator(object):
    # Cbr Page Locators

    TEXT_FIELD_NAME = 'MessageBody'
    I_AGREE_CHECKBOX_ID = '_agreementFlag'
    THREE_LINES_CLASS_NAME = 'burger'


class CbrPage(Browser):
    # Cbr Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def assert_partial_title(self, str):
        WebDriverWait(self.driver, 5).until(EC.title_contains(str))
        return str in self.get_page_title()

    def click_by_link_text(self, link_text):
        self.get_element(By.LINK_TEXT, link_text).click()

    def click_by_partial_link_text(self, link_text):
        self.get_element(By.PARTIAL_LINK_TEXT, link_text).click()

    def click_by_text(self, str):
        self.get_element(By.XPATH, f"//*[contains(text(), '{str}')]" ).click()

    def write_text_into_field(self, text):
        self.get_element(By.NAME, CbePageLocator.TEXT_FIELD_NAME).send_keys(text)

    def check_i_agree(self):
        self.get_element(By.ID, CbePageLocator.I_AGREE_CHECKBOX_ID).click()

    def make_a_screenshot(self, path):
        os.makedirs('screenshots')
        self.driver.save_screenshot(path)

    def press_three_lines_menu(self):
        self.get_element(By.CLASS_NAME, CbePageLocator.THREE_LINES_CLASS_NAME).click()

    def click_by_xpath(self, xpath):
        self.get_element(By.XPATH, xpath).click()

    def switch(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])
