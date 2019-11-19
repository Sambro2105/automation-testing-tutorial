class googleSearch():

    def __init__(self, driver):
        self.driver = driver

        self.searchbox_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
        self.google_search_button_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'
        self.request = 'Центральный банк РФ'

    def find_search_field(self):
        assert self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

    def type_request_into_searchbox(self):
        self.driver.find_element_by_xpath(self.google_search_button_xpath).send_keys(self.request)

    def click_search(self):
        self.driver.find_element_by_xpath(self.google_search_button_xpath).click()