from distutils.spawn import find_executable

import pytest
from tests.conftest import driver

def test_sidebar_hub_item(user_sidebar_fixture):
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field("qa_automation_password")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    page.click_log_in_button()
    page.click_later_button()
    page.click_menu_button()
    page.click_add_hub_button()
    page.should_be_hub_page()
    
def test_sidebar_settings_item(user_sidebar_fixture):
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field("qa_automation_password")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    page.click_log_in_button()
    page.click_later_button()
    page.click_menu_button()
    page.click_settings_button()
    page.should_be_settings_page()

def test_sidebar_help_item(user_sidebar_fixture):
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field("qa_automation_password")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    page.click_log_in_button()
    page.click_later_button()
    page.click_menu_button()
    page.click_help_button()
    page.should_be_help_page()

def test_sidebar_logs_item(user_sidebar_fixture):
    page = user_sidebar_fixture
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field("qa_automation_password")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    page.click_log_in_button()
    page.click_later_button()
    page.click_menu_button()
    page.click_logs_button()
    page.should_be_logs_page()

