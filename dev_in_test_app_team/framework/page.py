from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element: str):
        exceptions = (NoSuchElementException, StaleElementReferenceException,)
        return WebDriverWait(self.driver, 5, ignored_exceptions=exceptions)\
            .until(expected_conditions.element_to_be_clickable((By.ID, element)))

    def click_element(self, element):
        return element.click()

    def input_text(self, element, text):
        return element.send_keys(text)

    def log_out(self):
        self.find_element("com.ajaxsystems:id/menuDrawer").click()
        self.find_element("com.ajaxsystems:id/settings").click()
        self.find_element("com.ajaxsystems:id/accountInfoLogoutNavigate").click()
