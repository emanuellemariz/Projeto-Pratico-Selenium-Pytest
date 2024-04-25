from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class checkoutComplete(BasePage):
    CONFIRMATION_MESSAGE = (By.XPATH, "//div/h2[@class='complete-header']")


    def orderConfirmation(self):
        return self.driver.find_element(*self.CONFIRMATION_MESSAGE).text