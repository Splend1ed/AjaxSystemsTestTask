from dev_in_test_app_team.framework import LoginPage
from dev_in_test_app_team.log import get_logger


logger = get_logger()


class MainPage(LoginPage):
    def __init__(
            self,
            driver,
            sidebar_id: str,
            login_btn_id: str,
            login_field_id: str,
            password_field_id: str,
            button_next_id: str
    ):
        super().__init__(driver, login_btn_id, login_field_id, password_field_id, button_next_id)
        self.sidebar_id = sidebar_id

    def is_clickable_buttons(self, *args):
        buttons_ids = [*args]
        button_status = []
        for resource_id in buttons_ids:
            element = self.find_element(resource_id, 5)
            if element.get_attribute("clickable") == "true":
                logger.info("Element clickable")
                button_status.append(True)
            else:
                logger.error("Element not clickable")
                button_status.append(False)

        if False in button_status:
            return False
        return True

    def check_sidebar_buttons(self, add_hub_id, settings_id, help_id, repost_id, terms_id):
        off_notifications = self.find_element("com.ajaxsystems:id/cancel_button", 7)
        self.click_element(off_notifications)

        sidebar_btn = self.find_element(self.sidebar_id, 5)
        self.click_element(sidebar_btn)

        return self.is_clickable_buttons(
            add_hub_id, settings_id, help_id, repost_id, terms_id
        )
