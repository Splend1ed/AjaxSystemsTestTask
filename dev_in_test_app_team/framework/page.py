from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from dev_in_test_app_team.log import get_logger


logger = get_logger()


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element_id: str, wait_time):
        exceptions = (NoSuchElementException, StaleElementReferenceException,)
        try:
            element = WebDriverWait(self.driver, wait_time, ignored_exceptions=exceptions)\
                .until(expected_conditions.element_to_be_clickable((By.ID, element_id)))
            logger.info(f"Element '{element_id}' was found.")
            return element
        except TimeoutException:
            logger.error(f"Element '{element_id}' didnt found.")
            raise NoSuchElementException

    def click_element(self, element):
        logger.info(f"Element '{element.get_attribute('resource-id')}' was clicked.")
        return element.click()

    def input_text(self, element, text):
        logger.info(f"Inputted text '{text}' in field {element.get_attribute('resource-id')}.")
        return element.send_keys(text)

    def log_out(self):
        self.find_element("com.ajaxsystems:id/menuDrawer", 5).click()
        self.find_element("com.ajaxsystems:id/settings", 5).click()
        self.find_element("com.ajaxsystems:id/accountInfoLogoutNavigate", 5).click()
        logger.info(f"Logged out from app")
