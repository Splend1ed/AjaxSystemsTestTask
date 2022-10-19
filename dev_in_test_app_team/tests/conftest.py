import subprocess
import time

import pytest
from appium import webdriver

from dev_in_test_app_team.log import get_logger
from dev_in_test_app_team.utils.android_utils import android_get_desired_capabilities


logger = get_logger()


@pytest.fixture(scope="session")
def run_appium_server():
    subprocess.Popen(
        ["appium", "-a", "0.0.0.0", "-p", "4723", "--allow-insecure", "adb_shell"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True,
    )
    logger.info(f"Started appium server at 0.0.0.0:4723")
    time.sleep(2)


@pytest.fixture(scope="session")
def driver(run_appium_server):
    driver = webdriver.Remote(
        "http://localhost:4723/wd/hub", android_get_desired_capabilities()
    )
    logger.info(f"Started driver")
    yield driver
