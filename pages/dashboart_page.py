from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from .base_page import BasePage


class DashboartPage(BasePage):
    HEADER_TEXT = (By.XPATH, "//div/label/t[contains(text(), 'Тип клиента')]")
    SALES_BUTTON = (By.XPATH, "//li/a/span[contains(text(), 'Продажа')]")

    def check_page(self):
        assert "Тип клиента" in self.get_text(self.HEADER_TEXT), "Dashboart sahifa ochilmadi!"

    def click_button(self):
        try:
            # Element clickable bo'lguncha kutish
            wait = WebDriverWait(self.driver, 20)
            element = wait.until(EC.element_to_be_clickable(self.SALES_BUTTON))
            element.click()
        except ElementClickInterceptedException:
            # Elementni JavaScript yordamida bosish
            element = self.driver.find_element(*self.SALES_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            # Bloklovchi elementni kutish va yana urinib ko'rish
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "block-ui-overlay")))
            element = self.driver.find_element(*self.SALES_BUTTON)
            element.click()
