from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class cartPage(BasePage):
    REMOVE_BUTTON1 = (By.XPATH, "(//button[text()='Remove'])[1]")
    NUMBER_ITEMS = (By.XPATH, "//span[@class='shopping_cart_badge']")
    CHECKOUT_BUTTON = (By.NAME, "checkout")

    def remove_item(self):
        self.driver.find_element(*self.REMOVE_BUTTON1).click()

    def verifying_number_items(self):
        return self.driver.find_element(*self.NUMBER_ITEMS).text
    
    def checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
