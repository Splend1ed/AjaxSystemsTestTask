from selenium.common import InvalidSelectorException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .page import Page


class LoginPage(Page):
    def __init__(
            self,
            driver,
            login_btn: str,
            login_field: str,
            password_field: str,
            button_next: str
    ):
        super().__init__(driver)
        self.login_btn = login_btn
        self.login_field = login_field
        self.password_field = password_field
        self.button_next = button_next

    def login(self, email: str, password: str):
        login_btn = self.find_element(self.login_btn)
        login_btn.click()

        login_input = self.find_element(self.login_field)
        login_input.clear()
        self.input_text(login_input, email)

        password_input = self.find_element(self.password_field)
        password_input.clear()
        self.input_text(password_input, password)

        confirm_button = self.find_element(self.button_next)
        self.click_element(confirm_button)

        return self

    def is_loggined(self):
        try:
            self.find_element("com.ajaxsystems:id/cancel_button").click()
            return True

        except (NoSuchElementException, InvalidSelectorException, TimeoutException):
            return False




