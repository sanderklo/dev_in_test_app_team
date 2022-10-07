from .page import Page
from framework.locators import MainPageLocators


class SideBar(Page):
     
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

    def should_be_hub_page(self):
        assert self.is_element_shown(*MainPageLocators.HUB_PAGE), "You dont in hub page"

    def should_be_settings_page(self):
        assert self.is_element_shown(*MainPageLocators.SETTINGS_PAGE), "You dont in settings page"
    
    def should_be_help_page(self):
        assert self.is_element_shown(*MainPageLocators.HELP_PAGE), "You dont in help page"

    def should_be_logs_page(self):
        assert self.is_element_shown(*MainPageLocators.LOGS_PAGE), "You dont in logs page"