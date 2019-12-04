from selenium import webdriver

implicitly_wait_time = 10


def before_all(context):
    context.url = "http://todomvc.com/examples/react/"


def before_scenario(context, scenario):    # maybe I should use webdriver initialization with whole testrun scope,
    context.browser = webdriver.Chrome()   # but there is only 4 tests
    context.browser.implicitly_wait(implicitly_wait_time)


def after_scenario(context, scenario):
    context.browser.quit()
