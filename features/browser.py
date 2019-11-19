from selenium import webdriver

class Browser(object):

    driver = webdriver.Chrome(executable_path='\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.quit()