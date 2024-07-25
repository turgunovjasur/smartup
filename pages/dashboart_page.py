import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage


class DashboartPage(BasePage):
    # HEADER_TEXT = (By.XPATH, "//div/label/t[contains(text(), 'Тип клиента')]")
    HEADER_TEXT = (By.XPATH, "//div/h3[contains(text(), 'Trade')]")
    SALES_BUTTON = (By.XPATH, "//li/a/span[contains(text(), 'Продажа')]")

    def check_page(self):
        wait = WebDriverWait(self.driver, 20)  # 20 sekundgacha kutish
        try:
            element = wait.until(EC.presence_of_element_located(self.HEADER_TEXT))
            assert "Trade" in element.text, "Dashboart sahifa ochilmadi!"
        except:
            self.take_screenshot("dashboart_page_error")
            raise

    def click_button(self):
        time.sleep(5)
        self.click_element(self.SALES_BUTTON)
