import pytest
from selenium import webdriver 
from pages.base_page import BasePage
from pages.landing_page import landingPage
from pages.product_page import productPage
from pages.cart_page import cartPage
from pages.checkoutInfo_page import infoPage
from pages.checkoutOverview_page import checkoutOverview
from pages.checkoutComplete_page import checkoutComplete
from config.WebDriver_Singleton import WebDriverSingleton


@pytest.fixture()
def driver():
    driver = WebDriverSingleton.get_instance()
    BasePage(driver).go_to_site()
    print("Start")
    yield driver

@pytest.fixture(scope="session", autouse=True)
def quit_browser():
    yield
    print("End")
    WebDriverSingleton.quit_instance()
    

def test_happy_path(driver):


    step1 = landingPage(driver)
    step1.fill_landingPage("standard_user", "secret_sauce")
    
    step2 = productPage(driver)
    step2.add_products(5)

    cartNumber = step2.verifying_number_items()
    assert cartNumber == "6"

    step2.accessing_cart()

    step3 = cartPage(driver)
    step3.remove_item()

    cartNumber = step3.verifying_number_items()
    assert cartNumber == "5"

    step3.checkout_button()

    step4 = infoPage(driver)
    step4.personalInfo("Tester", "Silva", "62280000")

    step4.continueButton()

    step5 = checkoutOverview(driver)
    step5.finish_button()

    step6 = checkoutComplete(driver)
    message = step6.orderConfirmation()
    assert message == "Thank you for your order!"

    


def test_login_errormessage(driver):

    #Login using invalid user
    step1 = landingPage(driver)
    step1.fill_landingPage("standard", "secret_sauce")

    errorText = step1.loginError_message()
    displayError = errorText.is_displayed()
    assert displayError == True
      
   
def test_checkout_errormessage(driver):

    step1 = landingPage(driver)
    step1.fill_landingPage("standard_user", "secret_sauce")

    step2 = productPage(driver)
    step2.add_products(0) #Add 1 product in the cart

    step2.accessing_cart()

    step3 = cartPage(driver)
    step3.checkout_button()

    step4 = infoPage(driver)
    step4.continueButton()

    errorMessage = step4.errorMessage()
    displays = errorMessage.is_displayed()
    assert displays == True


def test_assert_low_to_high(driver):

    step1 = landingPage(driver)
    step1.fill_landingPage("standard_user", "secret_sauce")

    step2 = productPage(driver)
    step2.filter_list("Price (low to high)")

    prices = step2.get_prices()
    newPriceList = [] #Lista vazia que recebrá as string já modificadas dos elementos
    for nPrices in prices:
        textPrice = nPrices.text
        textPrice = textPrice.replace("$", "")
        newPriceList.append(float(textPrice))

    assert (newPriceList[0] < newPriceList[1]) == True

    






