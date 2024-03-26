import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print("Start")
    yield driver
    print("End")
    driver.quit()
    

def test_happy_path(driver):


    #Login using standard user
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password.send_keys("secret_sauce")

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()

    #Add 6 products in the cart
    addProduct = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    for item in addProduct:
        item.click()
        sleep(1)

    #Assert 6 products in the cart
    cartItems = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    assert cartItems == "6"

    #Access Cart
    cartButton = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cartButton.click()

    #Remove 1 product from Cart
    removeButton = driver.find_element(By.XPATH, "(//button[text()='Remove'])[1]")
    removeButton.click()

    sleep(1)

    #Assert 5 products in the cart
    cartItems = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    assert cartItems == "5"

    #Click on Checkout button
    checkoutButton = driver.find_element(By.NAME, "checkout")
    checkoutButton.click()

    #Fill the blanks in Checkout Page
    firstname = driver.find_element(By.ID, "first-name")
    firstname.send_keys("Tester")

    lastname = driver.find_element(By.ID, "last-name")
    lastname.send_keys("da Silva")

    postalcode = driver.find_element(By.ID, "postal-code")
    postalcode.send_keys("62280000")

    continueButton = driver.find_element(By.NAME, "continue")
    continueButton.click()

    #Click on Finish button
    finishButton = driver.find_element(By.ID, "finish")
    finishButton.click()

    sleep(1)

    #Assert confirmation message
    confirmationMessage = driver.find_element(By.XPATH, "//div/h2[@class='complete-header']").text
    assert confirmationMessage == "Thank you for your order!"


def test_login_errormessage(driver):

    #Login using invalid user
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username.send_keys("standard")

    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password.send_keys("secret_sauce")

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()

    sleep(1)

    #Assert login error message
    errorText = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    displayError = errorText.is_displayed()
    assert displayError == True  
   
def test_checkout_errormessage(driver):

    #Login using standard user
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password.send_keys("secret_sauce")

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()

    #Add 1 product in the cart
    addProduct = driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]")
    addProduct.click()

    #Access Cart
    cartButton = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cartButton.click()

    #Click on Checkout button
    checkoutButton = driver.find_element(By.NAME, "checkout")
    checkoutButton.click()

    #Click on Continue button
    continueButton = driver.find_element(By.NAME, "continue")
    continueButton.click()

    #Assert error message
    message =  driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
    displays = message.is_displayed()
    assert displays == True

def test_assert_low_to_high(driver):

    #Login using standard user
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password.send_keys("secret_sauce")

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()

    #Ordinate product list by Price (Low to High)
    filter = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    Select(filter).select_by_visible_text("Price (low to high)")

    sleep(1)

    #Assert product list is ordained as set
    price1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]").text
    price2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]").text
    nPrice1 = price1.replace("$", "")
    nPrice2 = price2.replace("$", "")

    value1 = float(nPrice1)
    value2 = float(nPrice2)
    
    assert (value1 < value2) == True






