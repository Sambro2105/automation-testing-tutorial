from nose.tools import assert_true
from behave import given, when, then

from features.pages.cbr_page import CbrPage
from features.pages.search_results_page import SearchResultsPage


@given('Title of the page is "{title}"')
def step_impl(context, title):
    context.search_results_page = SearchResultsPage()
    assert_true(context.search_results_page.is_page_title(title))

@when('I see "{url}" partial link')
def find_cbr_link(context, url):
    assert_true(context.search_results_page.is_there_a_search_result(url))

@then('I click on the "{url}"')
def click_on_the_link(context, url):
    context.search_results_page.click_on_search_result(url)