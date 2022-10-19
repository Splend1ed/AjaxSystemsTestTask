import pytest


@pytest.mark.parametrize(
    "expected",
    [
        (
            True
        )
    ]
)
def test_sidebar(user_sidebar_fixture, expected):
    main_page = user_sidebar_fixture.login(
        "qa.ajax.app.automation@gmail.com", "qa_automation_password"
    )
    is_clickable_btns = main_page.check_sidebar_buttons(
        "com.ajaxsystems:id/addHub", "com.ajaxsystems:id/settings",
        "com.ajaxsystems:id/help", "com.ajaxsystems:id/logs",
        "com.ajaxsystems:id/documentation_text"
    )
    assert is_clickable_btns == expected
