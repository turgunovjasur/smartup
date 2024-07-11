# from telnetlib import EC
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class CreateOrderPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/h3/t[contains(text(), 'Основное')]")
    WORKSPACE = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[1]")
    WORKSPACE_ELEM = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[1]/div/div/div[2]/b-input/div/div[2]/div[1]/div[1]/div')
    STAFF_UNIT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[2]")
    STAFF_UNIT_ELEM = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[1]/div/div/div[3]/div[1]/b-input/div/div[2]/div[2]/div[1]/div/div[1]')
    CLIENT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[3]")
    CLIENT_ELEM = (By.XPATH, '//*[@id="kt_content"]/div[2]/div/b-page/div/div/div/div/div/form[1]/div/div/div[4]/b-input/div/div[2]/div[2]/div[1]/div/div[2]')
    PROJECT = (By.XPATH, "(//div/input[@placeholder='Поиск...'])[4]")
    CONTRACT = (By.XPATH, "//div/input[@placeholder='Пароль']")
    NEXT_BUTTON = (By.XPATH, "//span/t[contains(text(), 'Далее')]")
    FIRST_BUTTON = (By.XPATH, "//b-input//div[contains(@class, 'hint-footer')][1]")

    def fill_form(self, workspace, staff_unit, client):
        self.new_input(self.WORKSPACE, workspace, self.WORKSPACE_ELEM)
        self.new_input(self.STAFF_UNIT, staff_unit, self.STAFF_UNIT_ELEM)
        self.new_input(self.CLIENT, client, self.CLIENT_ELEM)

    def check_page(self):
        wait = WebDriverWait(self.driver, 20)  # 20 sekundgacha kutish
        try:
            element = wait.until(EC.presence_of_element_located(self.HEADER_TEXT))
            assert "Основное" in element.text, f"Create_order_page Sahifa ochilmadi - {element.text}"
        except:
            self.take_screenshot("create_order_page_error")
            raise

    # def check_page(self):
    #     assert "Далее" in self.get_text(self.HEADER_TEXT), "Create_order_page Sahifa ochilmadi!"

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

