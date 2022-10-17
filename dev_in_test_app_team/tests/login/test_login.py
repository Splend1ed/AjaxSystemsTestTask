import pytest


@pytest.mark.parametrize(
    "email, password, expected",
    [
        (
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True
        ),
        (
            "bad_email",
            "bad_password",
            False
        ),
        (
            "bad_email",
            "qa_automation_password",
            False
        ),
        (
            "qa.ajax.app.automation@gmail.com",
            "bad_password",
            False
        ),
    ], ids=["correct credentials", "incorrect credentials", "incorrect email", "incorrect password"]

)
def test_user_login(user_login_fixture, email, password, expected):
    lg = user_login_fixture.login(
        email,
        password,
    )
    is_loggined = lg.is_loggined()
    assert is_loggined == expected
    if is_loggined:
        user_login_fixture.log_out()



