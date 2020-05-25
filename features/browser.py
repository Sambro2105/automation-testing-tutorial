from selenium import webdriver
import os


class Browser(object):
    path = os.path.join(os.getcwd(), 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=path)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self):
        self.driver.quit()