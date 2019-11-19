from nose.tools import assert_true
from behave import *
from features.pages.cbr_warning_page import CbrWarningPage

@given('I save warning text')
def save_warning_text(context):
    context.warning_page = CbrWarningPage()
    context.warning_text_ru = context.warning_page.get_text_from()


@when('I click on "{link_text}"')
def find_cbr_link(context, link_text):
    context.warning_page.click_by_text(link_text)

@when('I save new warning text')
def save_new_warning_text(context):
    context.warning_text_en = context.warning_page.get_text_from()

@then('I compare new warning text with the old')
def compare_warnings(context):
    assert_true(context.warning_text_en != context.warning_text_ru)

@then('I save a screenshot')
def save_screenshot(context):
    context.warning_page.save_screenshot(r'screenshots\2.png')