from distutils.spawn import find_executable
from re import fullmatch
from loguru import logger

import pytest
from tests.conftest import driver
logger.add("debug_test_sidebar.log", format="{time} {level} {message}", level="DEBUG")

@logger.catch
def test_sidebar_hub_item(user_sidebar_fixture):
    logger.debug("Starting test_sidebar_hub_item")
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    logger.debug("Tap on Log In button")
    page.wait()
    page.write_password_in_field("qa_automation_password")
    logger.debug("Writing password in login field")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    logger.debug("Writing mail in login field")
    page.click_log_in_button()
    logger.debug("Tap on Log In button")
    page.click_later_button()
    logger.debug("Tap on Later button")
    page.click_menu_button()
    logger.debug("Tap on Menu icon")
    page.click_add_hub_button()
    logger.debug("Tap on Add Hub button")
    page.wait()
    page.should_be_hub_page()
    logger.debug("Checking is that page wich need")
    logger.debug("Finish test_sidebar_hub_item\n")

@logger.catch   
def test_sidebar_settings_item(user_sidebar_fixture):
    logger.debug("Starting test_sidebar_settings_item")
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    logger.debug("Tap on Log In button")
    page.wait()
    page.write_password_in_field("qa_automation_password")
    logger.debug("Writing password in login field")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    logger.debug("Writing mail in login field")
    page.click_log_in_button()
    logger.debug("Tap on Log In button")
    page.click_later_button()
    logger.debug("Tap on Later button")
    page.click_menu_button()
    logger.debug("Tap on Menu icon")
    page.click_settings_button()
    logger.debug("Tap on Settings button")
    page.wait()
    page.should_be_settings_page()
    logger.debug("Checking is that page wich need")
    logger.debug("Finish test_sidebar_settings_item\n")

@logger.catch
def test_sidebar_help_item(user_sidebar_fixture):
    logger.debug("Starting test_sidebar_settings_item")
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    logger.debug("Tap on Log In button")
    page.wait()
    page.write_password_in_field("qa_automation_password")
    logger.debug("Writing password in login field")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    logger.debug("Writing mail in login field")
    page.click_log_in_button()
    logger.debug("Tap on Log In button")
    page.click_later_button()
    logger.debug("Tap on Later button")
    page.click_menu_button()
    logger.debug("Tap on Menu icon")
    page.click_help_button()
    logger.debug("Tap on Help button")
    page.wait()
    page.should_be_help_page()
    logger.debug("Checking is that page wich need")
    logger.debug("Finish test_sidebar_help_item\n")

@logger.catch
def test_sidebar_logs_item(user_sidebar_fixture):
    logger.debug("Starting test_sidebar_settings_item")
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    logger.debug("Tap on Log In button")
    page.wait()
    page.write_password_in_field("qa_automation_password")
    logger.debug("Writing password in login field")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    logger.debug("Writing mail in login field")
    page.click_log_in_button()
    logger.debug("Tap on Log In button")
    page.click_later_button()
    logger.debug("Tap on Later button")
    page.click_menu_button()
    logger.debug("Tap on Menu icon")
    page.click_logs_button()
    logger.debug("Tap on Logs button")
    page.wait()
    page.should_be_logs_page()
    logger.debug("Checking is that page wich need")
    logger.debug("Finish test_sidebar_logs_item\n")

