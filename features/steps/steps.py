from behave import *
from selenium.webdriver.common.keys import Keys
import page
from time import sleep


@given('the site is opened')
def step_impl(context):
    # context.browser = webdriver.Chrome()
    context.browser.get(context.url)
    pass


@when('i add "{text}" in input')
def step_impl(context, text):
    input_field = page.InputField(context.browser)
    input_field.add_text(text)  # todo implement text as flexible parameter from table


@step('press enter for text input')
def step_impl(context):
    page.InputField(context.browser).press_enter()


@then('the {integer} item in list should be "{text}"')
def step_impl(context, integer, text):
    item_index = int(integer) - 1
    assert page.ToDoList(context.browser).get_element_text_by_index(item_index) == text, print(
        "smth goes wrong, presented only this text: " + page.ToDoList(context.browser).
        get_element_text_by_index(item_index))


@then('counter at the bottom should shows {integer}')  # to do fix this "right" to flexible parameter
def step_impl(context, integer):
    items_number = int(integer)
    assert items_number == page.BottomCounter(context.browser).get_list_counter()


@given('i have three items in list')
def step_impl(context):
    item_list = ["Ответить на вопрос жизни, вселенной и всего такого", # to do fix this hardcode
                 "Придумать остроумные пункты",
                 "Погладить кошку"]
    create_item = page.InputField(context.browser)
    for item in item_list:
        create_item.create_new_item(item)


@when('i click completed button on second item')
def step_impl(context):
    second_item_index = 1
    page.CompletedButton(context.browser).toggle_button_by_index(second_item_index)


@then('this task should become completed')
def step_impl(context):
    this_task_index = 1
    assert page.ToDoList(context.browser).is_item_by_index_completed(this_task_index)


@then('i sleep')  # for debugging purposes only
def step_impl(context):
    sleep(10)


@when('i\'m changing the text of the third input to "{text}"')
def step_impl(context, text):
    third_item_index = 2
    page.ToDoList(context.browser).change_item_by_index(third_item_index, text)


