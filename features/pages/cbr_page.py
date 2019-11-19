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
        self.driver.find_element_by_link_text(link_text).click()

    def click_by_h2(self, str):
        self.driver.find_element_by_xpath(f"//*[contains(text(), '{str}')]" ).click()

    def write_text_into_field(self, text):
        self.driver.find_element_by_name(CbePageLocator.TEXT_FIELD_NAME).send_keys(text)

    def check_i_agree(self):
        self.driver.find_element_by_id(CbePageLocator.I_AGREE_CHECKBOX_ID).click()

    def make_a_screenshot(self, path):
        os.makedirs('screenshots')
        self.driver.save_screenshot(path)

    def press_three_lines_menu(self):
        self.driver.find_element_by_class_name(CbePageLocator.THREE_LINES_CLASS_NAME).click()

