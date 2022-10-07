from distutils.spawn import find_executable
from re import fullmatch
from loguru import logger
import pytest
from tests.conftest import driver


@logger.catch
def test_sidebar_menu(user_sidebar_fixture):
    page = user_sidebar_fixture
    logger.debug("Starting test_sidebar_menu")
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field("qa_automation_password")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    page.click_log_in_button()
    logger.debug("Going to main menu page")
    page.click_later_button()
    page.click_menu_button()
    logger.debug("Tap on 'Menu' icon")
    page.click_add_hub_button()
    logger.debug("Check 'Add Hub' button on sidebar menu")
    page.should_be_hub_page()
    page.back()
    page.click_menu_button()
    page.click_settings_button()
    logger.debug("Check 'Settings' button on sidebar menu")
    page.should_be_settings_page()
    page.back()
    page.click_menu_button()
    page.click_help_button()
    logger.debug("Check 'Help' button on sidebar menu")
    page.should_be_help_page()
    page.back()
    page.click_menu_button()
    page.click_logs_button()
    logger.debug("Check 'Logs' button on sidebar menu")
    page.wait()
    page.should_be_logs_page()
    logger.debug("Finish test_sidebar_menu\n")


