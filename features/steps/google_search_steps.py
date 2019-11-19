from nose.tools import assert_equal
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then

@given('I go to google.ru')
def step_impl(context):
    context.driver.get("https://google.ru")

@given('I see a searchbox')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    except NoSuchElementException:
        return False
    return True

@when('I type "{search_term}"')
def step_impl(context, search_term):
    context.driver.find_element_by_name("q").send_keys(search_term)


@when('I click Google Search')
def step_impl(context):
    context.driver.find_element_by_class_name('gNO89b').click()

@then('I see search results')
def step_impl(context):
    assert_equal(context.driver.title, 'Центральный банк РФ - Поиск в Google')