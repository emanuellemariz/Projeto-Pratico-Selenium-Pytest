from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class landingPage(BasePage):
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def fill_landingPage(self, username, password):
        self.waits(self.USERNAME).send_keys(username) #não necessita do find_element porque o waits já retorna o elemento
        self.driver.find_element(*self.PASSWORD).send_keys(password) #o * divide a dupla em dois parametros
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def loginError_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE)