from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class checkoutOverview(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
        