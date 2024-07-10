from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrdersPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//ul/li/a[contains(text(), 'Опросники')]")
    CREATE_BUTTON = (By.XPATH, "//div/button[contains(text(), 'Создать')]")
    COUNT = (By.XPATH, "//div[@class='sg-cell col-sm-4 ng-binding']/t[@class='ng-scope'][contains(text(), 'Кол-во сделок')]/following-sibling::text()")

    def check_page(self):
        assert "Опросники" in self.get_text(self.HEADER_TEXT), "Order_page Sahifa ochilmadi!"

    def check_count(self):
        return self.get_text(self.COUNT)

    def click_create_button(self):
        self.click_element(self.CREATE_BUTTON)
