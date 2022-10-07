from selenium.common.exceptions import NoSuchElementException
from framework.locators import StartPageLocators, LoginPageLocators
from tests.conftest import driver

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, how, what):
        assert self.driver.find_element(how, what), "Element not founded"

    def click_element(self, how, what):
        self.driver.find_element(how, what).click()

    def is_element_shown(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_not_shown(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return True
        return False

    def go_to_log_in_page(self):
        self.click_element(*StartPageLocators.LOGIN_BUTTON)

    def write_password_in_field(self, text):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(text)

    def write_mail_in_field(self, text):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(text)

    def click_log_in_button(self):
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
    
    def wait(self):
        self.driver.implicitly_wait(50)

    def back(self):
        self.driver.back()
