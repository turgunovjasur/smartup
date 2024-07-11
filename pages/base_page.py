import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].value='';", element)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # time.sleep(1)
        element.send_keys(text)
        self.driver.execute_script("arguments[0].click();", element)


    def input_form_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.execute_script(f"arguments[0].value='{text}';", element)

        element.send_keys(Keys.ENTER)

    def new_input(self, locator, text, elem):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].value='';", element)
        element.send_keys(text)
        self.click_element(elem)

    def new_wait_input(self, locator, elem):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(Keys.ENTER)
        time.sleep(5)
        self.click_element(elem)


    def choice(self, locator, elem):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.click_element(element)
        time.sleep(2)
        # e = self.wait.until(EC.visibility_of_element_located(elem))
        self.click_element(elem)



    def get_text(self, locator):
        return self.find_element(locator).text

    def take_screenshot(self, name):
        # screenshots papkasini yaratish (agar mavjud bo'lmasa)
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")