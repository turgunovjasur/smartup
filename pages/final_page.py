from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class FinalPage(BasePage):
    PAYMENT_TYPE_INPUT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[1]")
    STATUS_INPUT = (By.XPATH, "(//div/[contains(text(), 'Черновик'])[3]")
    WAYBILL_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")

    SAVE_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Сохранить')]")
    YES_BUTTON = (By.XPATH, "//div/button[contains(text(), 'да')]")

    def fill_form(self, payment_type, status):
        self.input_text(self.PAYMENT_TYPE_INPUT, payment_type)
        self.input_text(self.STATUS_INPUT, status)

    def click_save_button(self):
        self.click_element(self.SAVE_BUTTON)
        self.click_element(self.YES_BUTTON)
