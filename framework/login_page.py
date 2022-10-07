from .page import Page
from framework.locators import MainPageLocators


class LoginPage(Page):

    def should_be_main_page(self):
        assert self.is_element_shown(*MainPageLocators.MAIN_DISPLAY), "You dont in main page"

    def should_not_be_main_page(self):
        assert self.is_element_not_shown(*MainPageLocators.MAIN_DISPLAY), "You in main page"