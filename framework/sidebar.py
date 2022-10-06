from .page import Page
from selenium.common.exceptions import NoSuchElementException
from framework.locators import StartPageLocators, LoginPageLocators, MainPageLocators


class SideBar(Page):

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

    def go_to_log_in_page(self):
        self.click_element(*StartPageLocators.LOGIN_BUTTON)

    def write_password_in_field(self, text):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(text)

    def write_mail_in_field(self, text):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(text)

    def click_log_in_button(self):
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
        
    def click_later_button(self):
        self.click_element(*MainPageLocators.CHECK_LATER_BUTTON)

    def click_menu_button(self):
        self.click_element(*MainPageLocators.MENU_ICON)

    def click_add_hub_button(self):
        self.click_element(*MainPageLocators.ADD_HUB_ITEM)
    
    def click_settings_button(self):
        self.click_element(*MainPageLocators.SETTINGS_ITEM)

    def click_help_button(self):
        self.click_element(*MainPageLocators.HELP_ITEM)

    def click_logs_button(self):
        self.click_element(*MainPageLocators.LOGS_ITEM)

    def wait(self):
        self.driver.implicitly_wait(50)

    def should_be_hub_page(self):
        assert self.is_element_shown(*MainPageLocators.HUB_PAGE), "You dont in hub page"

    def should_be_settings_page(self):
        assert self.is_element_shown(*MainPageLocators.SETTINGS_PAGE), "You dont in settings page"
    
    def should_be_help_page(self):
        assert self.is_element_shown(*MainPageLocators.HELP_PAGE), "You dont in help page"

    def should_be_logs_page(self):
        assert self.is_element_shown(*MainPageLocators.LOGS_PAGE), "You dont in logs page"