from selenium.common import InvalidSelectorException, NoSuchElementException, TimeoutException

from .page import Page


class LoginPage(Page):
    def __init__(
            self,
            driver,
            login_btn_id: str,
            login_field_id: str,
            password_field_id: str,
            button_next_id: str,
    ):
        super().__init__(driver)
        self.login_btn_id = login_btn_id
        self.login_field_id = login_field_id
        self.password_field_id = password_field_id
        self.button_next_id = button_next_id

    def login(self, email: str, password: str):
        login_btn = self.find_element(self.login_btn_id, 10)
        self.click_element(login_btn)

        login_input = self.find_element(self.login_field_id, 10)
        login_input.clear()
        self.input_text(login_input, email)

        password_input = self.find_element(self.password_field_id, 5)
        password_input.clear()
        self.input_text(password_input, password)

        confirm_button = self.find_element(self.button_next_id, 5)
        self.click_element(confirm_button)

        return self

    def is_loggined(self):
        try:
            self.find_element("com.ajaxsystems:id/cancel_button", 7).click()
            return True

        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            return False
