from behave import *
from selenium import webdriver


@given('the site is opened')
def step_impl(context):
    # context.browser = webdriver.Chrome()
    url = 'http://todomvc.com/'
    context.browser.get(url)
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@then("we see the site")
def step_impl(context):
    assert True is not False


@when("i add text in input")
def step_impl(context):
    raise NotImplementedError(u'STEP: When i add text in input')