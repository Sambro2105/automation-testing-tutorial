from features.browser import Browser
from features.pages.google_search_page import SearchPage
from features.pages.search_results_page import SearchResultsPage

def before_all(context):
    context.browser = Browser()
    context.search_page = SearchPage()
    context.search_results_page = SearchResultsPage()

def after_all(context):
    context.browser.close()