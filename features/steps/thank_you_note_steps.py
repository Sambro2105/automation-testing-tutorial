from behave import *
from nose.tools import assert_true

from features.pages.cbr_page import CbrPage


@given('Page\'s title has "{str}"')
def assert_cbr_page(context, str):
    context.cbr_page = CbrPage()
    assert_true(context.cbr_page.assert_partial_title(str))


@when('I press "{str}"')
def press_link(context, str):
    context.cbr_page.click_by_text(str)


@when('I open "{str}" section')
def press_section(context, str):
    context.cbr_page.click_by_text(str)


@when('Enter "{text}" into the field')
def write_note_into_the_field(context, text):
    context.cbr_page.write_text_into_field(text)


@when('Check "Я согласен"')
def check_i_agree(context):
    context.cbr_page.check_i_agree()


@then("I make a screenshot")
def make_a_screenshot(context):
    context.cbr_page.make_a_screenshot(r'screenshots\1.png')