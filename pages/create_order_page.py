import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class CreateOrderPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h3/t[contains(text(), 'Основное')]")
    WORKSPACE = (By.XPATH, "//div[2]/div/div[8]/div")
    STAFF_UNIT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[2]")
    CLIENT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[3]")

    NEXT_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Далее')]")

    def check_page(self):
        assert "Основное" in self.get_text(self.HEADER_TEXT), "Create_order_page Sahifa ochilmadi!"

    def fill_form(self, workspace, staff_unit, client):
        self.input_text(self.WORKSPACE, workspace)
        time.sleep(5)
        self.input_text(self.STAFF_UNIT, staff_unit)
        time.sleep(5)
        self.input_text(self.CLIENT, client)
        time.sleep(5)

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

