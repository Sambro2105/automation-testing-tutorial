from behave import *
from nose.tools import assert_true
from features.pages.cbr_warning_page import CbrWarningPage
from features.pages.cbr_page import CbrPage


@when("I press three lines menu")
def press_three_lines_menu(context):
    context.cbr_page = CbrPage()
    context.cbr_page.press_three_lines_menu()


@when('I open "О сайте" section')
def click_on_warning(context):
    context.cbr_page.click_by_xpath('//*[@id="page"]/div[6]/div/div[4]/div[1]/ul/li[20]/a')


@step('I click on link "Предупреждение"')
def click_on_warning(context):
    context.cbr_page.click_by_xpath('//*[@id="page"]/div[6]/div/div[4]/div[21]/div[1]/ul/li[3]/div/a')
    context.cbr_page.switch()


@then('Title of the page is "{title}"')
def assert_page_title(context, title):
    context.cbr_warning_page = CbrWarningPage()
    assert_true(context.cbr_warning_page.get_page_title() == title)