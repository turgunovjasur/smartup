from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class GoodsPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//li/a[contains(text(), 'Товар')]")

    NAME_INPUT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[7]")
    QTY_INPUT = (By.XPATH, "(//div/input[@ng-if='item.product_id'])[1]")

    NEXT_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Далее')]")

    def check_modal(self):
        assert "Товар" in self.get_text(self.HEADER_TEXT), "Goods_page sahifasi ochilmadi!"

    def fill_form(self, name, qty):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.QTY_INPUT, qty)

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
