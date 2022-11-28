from pageObjects.DriverActions import DriverActions
from selenium.webdriver.common.by import By


class ProductPage(DriverActions):
    # Object repositories or webelements locator which are related to Product page are stored here
    button_addtocart_id = "add-to-cart-button"
    button_buynow_name = "submit.buy-now"
    text_addedtocart_xpath = "//*[@id='attachDisplayAddBaseAlert']/span"
    by_locator_addtocart_btn = (By.ID, button_addtocart_id)

    def __init__(self, driver):
        super().__init__(driver)

    def addToCart(self):        # Product is added to cart
        self.click_button(self.by_locator_addtocart_btn)

    def validateAddToCart(self):     # Method to find whether "added to cart" is present on screen or not
        if len(self.driver.find_elements("xpath", self.text_addedtocart_xpath)) > 0:
            return True
        else:
            return False
