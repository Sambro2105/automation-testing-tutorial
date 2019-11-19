from nose.tools import assert_true
from behave import *

from features.pages.google_search_page import SearchPage


@given('I go to "{url}"')
def step_impl(context, url):
    context.search_page = SearchPage()
    context.search_page.navigate(url)

@given('I see a searchbox')
def step_impl(context):
    assert_true(context.search_page.is_there_a_searchbox())

@when('I type "{request}"')
def step_impl(context, request):
    context.search_page.type_search_request(request)


@then('I click Google Search')
def step_impl(context):
    context.search_page.click_search()