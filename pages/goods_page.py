from telnetlib import EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class GoodsPage(BasePage):
    NAME_INPUT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[7]")
    NAME_ELEM = (By.XPATH, '//*[@id="inventory_goods_219"]/div[2]/b-pg-grid/div/div/div[1]/div[2]/div/div[1]/div/b-input/div/div[2]/div[2]/div[1]/div/div[1]')
    QTY_INPUT = (By.XPATH, "(//div/input[@ng-if='item.product_id'])[1]")
    NEXT_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Далее')]")

    def fill_form(self, qty):
        self.new_wait_input(self.NAME_INPUT, self.NAME_ELEM)
        self.input_text(self.QTY_INPUT, qty)

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
