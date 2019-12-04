from selenium import webdriver
from behave import fixture, use_fixture
from time import sleep

implicitly_wait_time = 10


def before_all(context):
    context.url = "http://todomvc.com/examples/react/"


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(implicitly_wait_time)


def after_scenario(context, scenario):
    context.browser.quit()
