# base_page.py
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.driver.save_screenshot("element_not_found.png")
            raise

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            self.driver.save_screenshot("element_not_clickable.png")
            raise

    def input_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            self.driver.save_screenshot("element_not_visible.png")
            raise

    def get_text(self, locator):
        try:
            return self.find_element(locator).text
        except TimeoutException:
            self.driver.save_screenshot("element_text_not_found.png")
            raise
