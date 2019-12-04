from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

input_css = "input.new-todo"
list_element_css = "ul.todo-list>li"
todo_counter_css = "span.todo-count > strong"
complete_button_css = "input.toggle"
completed_element_class = "completed"
any_filter_button_css = ".todoapp ul.filters a[href*='{}']"


class PageElement(object):

    def __init__(self, driver):
        self.driver = driver


class InputField(PageElement):

    def _return_input_field(self):
        input_field = self.driver.find_element_by_css_selector(input_css)
        return input_field

    def add_text(self, item_name):
        self._return_input_field().send_keys(item_name)

    def press_enter(self):
        self._return_input_field().send_keys(Keys.ENTER)

    def create_new_item(self, item_name):
        self.add_text(item_name)
        self.press_enter()


class ToDoList(PageElement):

    def _return_list_elements(self):
        items_list = self.driver.find_elements_by_css_selector(list_element_css)
        if len(items_list) != 0:
            return self.driver.find_elements_by_css_selector(list_element_css)
        else:
            raise NoSuchElementException

    def get_number_of_items(self):
        return len(self._return_list_elements())

    def get_element_by_index(self, index):
        return self._return_list_elements()[index]

    def get_element_text_by_index(self, index):
        return self._return_list_elements()[index].text  # todo check what if I put wrong index

    def is_item_by_index_completed(self, index):
        if self._return_list_elements()[index].get_attribute("class") == completed_element_class:
            return True
        else:
            return False

    def change_item_by_index(self, index, text):
        item_to_change = self._return_list_elements()[index]
        action_chains = ActionChains(self.driver)
        action_chains.double_click(item_to_change).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).\
            send_keys(text).send_keys(Keys.ENTER).perform()


class BottomCounter(PageElement):
    def get_list_counter(self):
        return int(self.driver.find_element_by_css_selector(todo_counter_css).text)


class CompletedButton(PageElement):

    # def __init__(self, driver, index):
    #     super(CompletedButton, self).__init__(driver) #  todo better inheritance from the list item class
    # self.button =

    def _get_button_by_index(self, index):
        button = ToDoList(self.driver).get_element_by_index(index).find_element_by_css_selector(complete_button_css)
        return button

    def toggle_button_by_index(self, index):
        self._get_button_by_index(index).click()


class LowFilterButton(PageElement):
    possible_filters = {"All": "", "Active": "active", "Completed": "completed"}

    def __init__(self, driver, filter_name):
        super().__init__(driver)
        self.filter_css_name = self.possible_filters[filter_name]
        self.filter_locator = any_filter_button_css.format(self.filter_css_name)

    def click_filter_menu_item(self):
        self.driver.find_element_by_css_selector(self.filter_locator).click()
