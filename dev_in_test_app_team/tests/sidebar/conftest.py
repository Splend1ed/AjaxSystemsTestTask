import pytest

from dev_in_test_app_team.framework.main_page import MainPage


@pytest.fixture(scope="function")
def user_sidebar_fixture(driver):
    yield MainPage(
        driver=driver,
        sidebar_id="com.ajaxsystems:id/menuDrawer",
        login_btn_id="com.ajaxsystems:id/login",
        login_field_id="com.ajaxsystems:id/login",
        password_field_id="com.ajaxsystems:id/password",
        button_next_id="com.ajaxsystems:id/next"
    )
