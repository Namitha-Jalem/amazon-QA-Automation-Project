from pageObjects.CommonFunctions import CommonFunctions
from pageObjects.DriverActions import DriverActions
from selenium.webdriver.common.by import By


class SearchPage(DriverActions):
    # Object repositories or webelements locator which are related to Search page are stored here
    textbox_min_id = "low-price"
    textbox_max_name = "high-price"
    button_go_xpath = "//*[@id='a-autoid-1']/span/input"
    linklist_selecteditems_xpath = "//div[@data-component-type='s-search-result']//span[@class='a-size-medium a-color-base a-text-normal']"
    priceList_filteredproducts_xpath = "//span[@class='a-price-whole']"
    text_selectedproductname_xpath = "//span[@id = 'productTitle']"
    by_locator_go_btn = (By.XPATH, button_go_xpath)
    by_locator_link_btn = (By.XPATH, linklist_selecteditems_xpath)
    by_locator_max_price_txt = (By.NAME, textbox_max_name)

    def __init__(self, driver):
        super().__init__(driver)

    def setMaxPriceText(self, max_text):        # Set the max price as 20,000
        self.driver.find_element("id", self.textbox_max_name).clear()
        self.send_values(self.by_locator_max_price_txt, max_text)
        self.click_button(self.by_locator_go_btn)

    def selectingProduct(self, product_number):  # selects the 3rd product
        self.click_element_list(self.by_locator_link_btn, product_number)

    def getProductName(self, product_number):   # Captures the 3rd product name
        list_of_products = self.driver.find_elements("xpath", self.linklist_selecteditems_xpath)
        # print(list_of_products[product_number].text)
        return list_of_products[product_number].text

    def validateProductName(self, product_name):  # Compares the product names from search result with 3rd selected product
        # After selecting the product
        selected_product_name = self.driver.find_element("xpath", self.text_selectedproductname_xpath).text
        # print(selectedProductName)
        if selected_product_name == product_name:
            return True
        else:
            return False

    def validatePrices(self, max_price):    # Compare the prices whether the filtered products are belong the range 20,000
        filtered_products_price_list = self.driver.find_elements("xpath", self.priceList_filteredproducts_xpath)
        cf = CommonFunctions(self.driver)
        for x in range(5):
            price_string = filtered_products_price_list[x].text
            price_integer = cf.convertPriceIntoInteger(price_string)
            if price_integer > max_price:
                return False
        return True
