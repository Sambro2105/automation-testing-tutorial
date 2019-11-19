from nose.tools import assert_equal
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then

@given('I go to "{url}"')
def step_impl(context, url):
    context.search_page.navigate(url)

@given('I see a searchbox')
def step_impl(context):
    try:
        context.search_page.find_searchbox()
    except NoSuchElementException:
        return False
    return True

@when('I type "{request}"')
def step_impl(context, request):
    context.search_page.type_search_request(request)


@when('I click Google Search')
def step_impl(context):
    context.search_page.click_search()

@then('I see search results')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), 'Центральный банк РФ - Поиск в Google')