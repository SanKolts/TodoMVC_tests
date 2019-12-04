from behave import *
from selenium.webdriver.common.keys import Keys
import page
from time import sleep


@given('the site is opened')
def step_impl(context):
    context.browser.get(context.url)
    pass


@when('I add "{text}" in input')
def step_impl(context, text):
    input_field = page.InputField(context.browser)
    input_field.add_text(text)  # todo implement text as flexible parameter from the table


@step('press enter for text input')
def step_impl(context):
    page.InputField(context.browser).press_enter()


@then('the {number} item in the list should be "{text}"')
def step_impl(context, number, text):
    item_index = int(number) - 1
    assert page.ToDoList(context.browser).get_element_text_by_index(item_index) == text, print(
        "smth goes wrong, presented only this text: " + page.ToDoList(context.browser).
        get_element_text_by_index(item_index))


@then('counter at the bottom should show {integer}')  # to do fix this "right" to flexible parameter
def step_impl(context, integer):
    items_number = int(integer)
    assert items_number == page.BottomCounter(context.browser).get_list_counter()


@given('I have three items in list')
def step_impl(context):
    item_list = ["Ответить на вопрос жизни, вселенной и всего такого", # to do fix this hardcode
                 "Придумать остроумные пункты",
                 "Погладить кошку"]
    create_item = page.InputField(context.browser)
    for item in item_list:
        create_item.create_new_item(item)


@when('I click completed button on second item')
def step_impl(context):
    second_item_index = 1
    page.CompletedButton(context.browser).toggle_button_by_index(second_item_index)


@then('this task should become completed')
def step_impl(context):
    this_task_index = 1
    assert page.ToDoList(context.browser).is_item_by_index_completed(this_task_index)


@then('I sleep')  # for debugging purposes only
def step_impl(context):
    sleep(10)


@when('I change the text of the third input to "{text}"')  # todo fix this hardcode "third"
def step_impl(context, text):
    third_item_index = 2
    page.ToDoList(context.browser).change_item_by_index(third_item_index, text)


@when('I click "{text}" filter button')
def step_impl(context, text):
    """
    'text' can be only "All", "Active" or "Completed"
    """
    page.LowFilterButton(context.browser, text).click_filter_menu_item()


@then('I should see {number} items in todolist')
def step_impl(context, number):
    todo_list = page.ToDoList(context.browser)
    assert int(number) == todo_list.get_number_of_items(), \
        print("expected: " + str(number) + "but received: " + str(todo_list.get_number_of_items()))


@then("not one task is not completed")
def step_impl(context):
    number_of_active_items = 0
    todo_list = page.ToDoList(context.browser)
    for index in range(todo_list.get_number_of_items()):
        if not todo_list.is_item_by_index_completed(index):
            number_of_active_items += 1
        else:
            raise Exception("completed task in list")