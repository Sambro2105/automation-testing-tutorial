from behave import given, when, then
from selenium import webdriver

driver = webdriver.Chrome(executable_path='\chromedriver.exe')

@given(u'"{url}" opens')
def google_opens(context, url):
    driver.get(url)
    context.driver = driver

@when(u'User sees a search field')
def search_field_has_appeared(context):
    assert context.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

@then(u'User types "{request}" into the search field')
def user_types_search_request(context, request):
    context.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(request)

@then(u'User clicks Google Search')
def user_clicks_google_search(context):
    context.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()

driver.quit()