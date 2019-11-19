import os

from features.browser import Browser
import shutil

def before_all(context):
    if os.path.isdir(os.getcwd() + 'screenshots'):
        shutil.rmtree(os.getcwd() + '\screenshots')
    context.browser = Browser()

def after_all(context):
    context.browser.close()