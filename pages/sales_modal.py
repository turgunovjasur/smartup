from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class SalesModal(BasePage):
    HEADER_TEXT = (By.XPATH, "//h3/span[contains(text(), 'Продажа')]")
    ORDERS_BUTTON = (By.XPATH, "//a/span[contains(text(), 'Заказы')]")

    def check_modal(self):
        try:
            assert "Продажа" in self.get_text(self.HEADER_TEXT), "Sales_modal sahifasi ochilmadi!"
        except AssertionError:
            self.driver.save_screenshot("sales_modal_not_opened.png")
            raise

    def click_button(self):
        self.click_element(self.ORDERS_BUTTON)
