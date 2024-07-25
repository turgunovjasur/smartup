import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class GoodsPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h3/t[contains(text(), 'ТМЦ')]")

    NAME_INPUT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[7]")
    # NAME_ELEM = (By.XPATH, '//*[@id="inventory_goods_219"]/div[2]/b-pg-grid/div/div/div[1]/div[2]/div/div[1]/div/b-input/div/div[2]/div[2]/div[1]/div/div[1]')
    NAME_ELEM = (By.XPATH, "(//div[@class = 'col-sm-12 ng-binding'])[1]")
    QTY_INPUT = (By.XPATH, "(//div/input[@ng-if='item.product_id'])[1]")

    NEXT_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Далее')]")

    def check_page(self):
        wait = WebDriverWait(self.driver, 20)  # 20 sekundgacha kutish
        try:
            element = wait.until(EC.presence_of_element_located(self.HEADER_TEXT))
            assert "ТМЦ" in element.text, f"goods_page Sahifa ochilmadi - {element.text}"
        except:
            self.take_screenshot("goods_pagee_error")
            raise

    def fill_form(self, qty):
        self.new_wait_input(self.NAME_INPUT, self.NAME_ELEM)
        time.sleep(5)
        self.input_form_text(self.QTY_INPUT, qty)

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
