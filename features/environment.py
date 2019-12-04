from selenium.webdriver import Chrome
from behave import fixture, use_fixture
from time import sleep


def before_feature(context):
    context.browser = Chrome()
    print("I'm started")


def after_all(context):
    print("I'm finished")
    context.browser.quit()
