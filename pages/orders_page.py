from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrdersPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//ul/li/a[contains(text(), 'Опросники')]")
    CREATE_BUTTON = (By.XPATH, "//div/button[contains(text(), 'Создать')]")
    COUNT = (By.XPATH, "//div[contains(@class, 'sg-sub-row')]/div[contains(@class, 'sg-cell')]/t[contains(text(), 'Кол-во сделок')]/../text()")

    def check_page(self):
        assert "Опросники" in self.get_text(self.HEADER_TEXT), "Order_page Sahifa ochilmadi!"

    def check_count(self):
        count_text = self.find_element(self.COUNT).text.strip()
        return int(count_text)  # Sonni integer ga aylantiramiz

    def click_create_button(self):
        self.click_element(self.CREATE_BUTTON)
