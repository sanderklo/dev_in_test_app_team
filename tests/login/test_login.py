from distutils.spawn import find_executable
from loguru import logger
import pytest
from tests.conftest import driver

class TestLoginPage():
    @logger.catch
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, user_login_fixture):
        self.page = user_login_fixture
        self.page.go_to_log_in_page()
        self.page.wait()

    def test_user_login(self):
        logger.debug("Start test_user_login")
        self.page.write_password_in_field("qa_automation_password")
        self.page.write_mail_in_field("qa.ajax.app.automation@gmail.com")
        logger.debug("Writing correct mail and password in login field")
        self.page.click_log_in_button()
        self.page.should_be_main_page()
        logger.debug("Checking that user can login in app")
        logger.debug("Finish test_user_login\n")

    @pytest.mark.parametrize('password, mail', [("qa_automation_password", ""),
                                                ("", "qa.ajax.app.automation@gmail.com"),
                                                ("password", "test@gmail.com")])
    def test_user_not_login(self, password, mail):
        self.page.write_password_in_field(password)
        self.page.write_mail_in_field(mail)
        logger.debug("Writing incorrect mail and password in login field")
        self.page.click_log_in_button()
        self.page.should_not_be_main_page()
        logger.debug("Checking that user cant login in app")
        logger.debug("Finish test_user_not_login\n")