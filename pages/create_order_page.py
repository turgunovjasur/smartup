from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class CreateOrderPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h3/t[contains(text(), 'Основное')]")
    WORKSPACE = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[1]")
    STAFF_UNIT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[2]")
    CLIENT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[3]")
    PROJECT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[4]")
    CONTRACT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    NEXT_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Далее')]")

    def fill_form(self, workspace, staff_unit, client):
        self.input_text(self.WORKSPACE, workspace)
        self.input_text(self.STAFF_UNIT, staff_unit)
        self.input_text(self.CLIENT, client)

    def check_page(self):
        assert "Основное" in self.get_text(self.HEADER_TEXT), "Create_order_page Sahifa ochilmadi!"

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

