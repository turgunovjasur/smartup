from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class FinalPage(BasePage):
    # PAYMENT_TYPE_INPUT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[1]")
    PAYMENT_TYPE_INPUT = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[3]/div/div[2]/div/div/div[2]/b-input/div/div[1]/div/input')
    PAYMENT_ELEM = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[3]/div/div[2]/div/div/div[2]/b-input/div/div[2]/div[1]/div/div')
    STATUS_INPUT = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[3]/div/div[3]/div/div/div[6]/div')
    STATUS_ELEM = (By.XPATH, '//*[@id="ui-select-choices-row-4-0"]/span')
    WAYBILL_INPUT = (By.XPATH, "//div/input[@placeholder='Пароль']")

    SAVE_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Сохранить')]")
    YES_BUTTON = (By.XPATH, "//div/button[contains(text(), 'да')]")

    def fill_form(self, payment_type, status):
        self.new_input(self.PAYMENT_TYPE_INPUT, payment_type, self.PAYMENT_ELEM)
        self.choice(self.STATUS_INPUT, self.STATUS_ELEM)

    def click_save_button(self):
        self.click_element(self.SAVE_BUTTON)
        self.click_element(self.YES_BUTTON)
