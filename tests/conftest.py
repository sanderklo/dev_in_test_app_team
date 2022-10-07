import subprocess
import time
from loguru import logger
import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities
logger.add(".debug_test_login.log", format="{time} {level} {message}", level="DEBUG")

@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='function')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    yield driver
    driver.quit()
 