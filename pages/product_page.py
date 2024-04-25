from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class productPage(BasePage):
    PRODUCT_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    NUMBER_ITEMS = (By.XPATH, "//span[@class='shopping_cart_badge']")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    FILTER = (By.XPATH, "//select[@class='product_sort_container']")
    PRICES = (By.XPATH, "//div[@class='inventory_item_price']")

    def add_products(self, NumberOfItems):
        products = self.driver.find_elements(*self.PRODUCT_BUTTONS)
        breakpt = products[NumberOfItems]
        for x in products:
            x.click()
            if x == breakpt: break

    def filter_list(self, Filter_Type):
        filter = self.driver.find_element(*self.FILTER)
        Select(filter).select_by_visible_text(Filter_Type)

    def verifying_number_items(self):
        return self.driver.find_element(*self.NUMBER_ITEMS).text
        
    def accessing_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def get_prices(self):
        return self.driver.find_elements(*self.PRICES)