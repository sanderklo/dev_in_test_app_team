from distutils.spawn import find_executable

import pytest
from framework.locators import StartPageLocators, LoginPageLocators, MainPageLocators
from tests.conftest import driver


def test_user_login(user_login_fixture):
    page = user_login_fixture
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field("qa_automation_password")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    page.click_log_in_button()
    page.should_be_main_page()

@pytest.mark.parametrize('password, mail', [("qa_automation_password", ""),
                                            ("", "qa.ajax.app.automation@gmail.com"),
                                            ("password", "test@gmail.com")])
def test_user_not_login(user_login_fixture, password, mail):
    page = user_login_fixture
    page.go_to_log_in_page()
    page.wait()
    page.write_password_in_field(password)
    page.write_mail_in_field(mail)
    page.click_log_in_button()
    page.should_not_be_main_page()