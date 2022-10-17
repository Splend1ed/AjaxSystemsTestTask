import pytest

from dev_in_test_app_team.framework.login_page import LoginPage


@pytest.fixture(scope="function")
def user_login_fixture(driver):
    yield LoginPage(
        driver,
        "com.ajaxsystems:id/login",
        "com.ajaxsystems:id/login",
        "com.ajaxsystems:id/password",
        "com.ajaxsystems:id/next"
    )



