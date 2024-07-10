from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboartPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/label/t[contains(text(), 'Тип клиента')]")
    SALES_BUTTON = (By.XPATH, "//li/a/span[contains(text(), 'Продажа')]")

    def check_page(self):
        assert "Тип клиента" in self.get_text(self.HEADER_TEXT), "Dashboart sahifa ochilmadi!"

    def click_button(self):
        self.click_element(self.SALES_BUTTON)
