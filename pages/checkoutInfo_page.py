from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class infoPage(BasePage):
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTALCODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.NAME, "continue")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")

    def personalInfo(self, firstname, lastname, postalcode):
        self.waits(self.FIRSTNAME).send_keys(firstname)
        self.driver.find_element(*self.LASTNAME).send_keys(lastname)
        self.driver.find_element(*self.POSTALCODE).send_keys(postalcode)

    def continueButton(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
    
    def errorMessage(self):
        return self.driver.find_element(*self.ERROR_MESSAGE)