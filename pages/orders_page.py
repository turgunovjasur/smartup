import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage


class OrdersPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//ul/li/a[contains(text(), 'Опросники')]")
    CREATE_BUTTON = (By.XPATH, "//div/button[contains(text(), 'Создать')]")
    COUNT = (By.XPATH, "//div[contains(@class, 'sg-cell') and contains(@class, 'col-sm-4') and contains(@class, 'ng-binding')]")

    def check_page(self):
        wait = WebDriverWait(self.driver, 20)  # 20 sekundgacha kutish
        try:
            element = wait.until(EC.presence_of_element_located(self.HEADER_TEXT))
            assert "Опросники" in element.text, "Order_page sahifa ochilmadi!"
        except:
            self.take_screenshot("Order_page_error")
            raise

    def check_count(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            element = wait.until(EC.presence_of_element_located(self.COUNT))
            count_text = element.text.strip()
            if count_text:
                # Faqat raqamlarni ajratib olish
                count = ''.join(filter(str.isdigit, count_text))
                return int(count) if count else 0
            else:
                print("Warn: hisoblash elementi bo'sh")
                return 0
        except Exception as e:
            print(f"Check_count-dagi xato: {str(e)}")
            self.take_screenshot("check_count_error")
            return 0

    # def check_count(self):
    #     element = self.find_element(self.COUNT)
    #     return int(element.text.split()[-1])  # So'nggi sonni olish

    def click_create_button(self):
        time.sleep(2)
        self.click_element(self.CREATE_BUTTON)
