from distutils.spawn import find_executable
from loguru import logger

import pytest
from framework.locators import StartPageLocators, LoginPageLocators, MainPageLocators
from tests.conftest import driver
logger.add("debug_test_login.log", format="{time} {level} {message}", level="DEBUG")

def test_user_login(user_login_fixture):
    logger.debug("Starting test_user_login")
    page = user_login_fixture
    page.go_to_log_in_page()
    logger.debug("Tap on Log In button")
    page.wait()
    page.write_password_in_field("qa_automation_password")
    logger.debug("Writing password in login field")
    page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
    logger.debug("Writing mail in login field")
    page.click_log_in_button()
    logger.debug("Tap on Log In button")
    page.should_be_main_page()
    logger.debug("Checking is that page wich need")
    logger.debug("Finish test_user_login\n")

@pytest.mark.parametrize('password, mail', [("qa_automation_password", ""),
                                            ("", "qa.ajax.app.automation@gmail.com"),
                                            ("password", "test@gmail.com")])
def test_user_not_login(user_login_fixture, password, mail):
    logger.debug("Starting test_user_not_login")
    page = user_login_fixture
    page.go_to_log_in_page()
    logger.debug("Tap on Log In button")
    page.wait()
    page.write_password_in_field(password)
    logger.debug("Writing password in login field")
    page.write_mail_in_field(mail)
    logger.debug("Writing mail in login field")
    page.click_log_in_button()
    logger.debug("Tap on Log In button")
    page.should_not_be_main_page()
    logger.debug("Checking is user not login")
    logger.debug("Finish test_user_not_login\n")