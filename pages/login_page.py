import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .dashboart_page import DashboartPage


class LoginPage(BasePage):
    LOGIN_INPUT = (By.XPATH, "//div/input[@placeholder='Логин@компания']")
    PASSWORD_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    SIGN_UP_BUTTON = (By.XPATH, "//div/button[contains(text(), 'Войти')]")

    def fill_registration_form(self, email, password):
        self.input_text(self.LOGIN_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)

    def click_sign_up_button(self):
        self.click_element(self.SIGN_UP_BUTTON)

    ERROR_MESSAGE = (By.XPATH, "//div/span[@id='error']")

    def is_error_message_displayed(self):
        return self.is_element_visible(self.ERROR_MESSAGE)

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def login(self, email, password):
        self.fill_registration_form(email, password)
        self.click_sign_up_button()
        time.sleep(5)

    def is_dashboard_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(  # Kutish vaqtini 20 sekundgacha
                EC.presence_of_element_located(DashboartPage.HEADER_TEXT)
            )
            return True
        except TimeoutException:
            print("Dashboard element topilmadi")  # Debuglash uchun
            self.take_screenshot("dashboard_not_found")  # Muammoni ko'rish uchun screenshot
            return False

    def take_error_screenshot(self):
        self.take_screenshot(f"login_error_{int(time.time())}")