import time

from selenium import webdriver
from pageObjects.Homepage import Homepage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductPage import ProductPage
from pageObjects.CommonFunctions import CommonFunctions
from pageObjects.DriverActions import DriverActions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001Search:
    driver = webdriver.Chrome()
    baseURL = ReadConfig.getApplicationURL()
    searchText = "Samsung phone"
    maxPriceText = 20000
    productNumber = 3

    logger = LogGen.loggen()

    def test_search(self):
        self.logger.info("******** Searching the Product ******* ")
        self.driver = Test001Search.driver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.hp = Homepage(self.driver)
        self.hp.setSearchText(self.searchText)
        actual_title = self.driver.title
        time.sleep(5)
        if actual_title == 'Amazon.in : Samsung phone':
            self.logger.info("******** Successfully validated the search action  ******* ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search.png")
            self.logger.error("******** Search action validation failed ******* ")
            assert False

    def test_filter(self):
        self.logger.info("******** Filtering the mobile phones ******* ")
        self.driver = Test001Search.driver
        self.sp = SearchPage(self.driver)
        self.sp.setMaxPriceText(self.maxPriceText)
        time.sleep(5)
        if self.sp.validatePrices(self.maxPriceText):
            self.logger.info("******** Successfully validated the filter action  ******* ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search.png")
            self.logger.error("******** filter action validation failed  ******* ")
            assert False

    def test_selectProduct(self):
        self.logger.info("******** Selecting the 3rd product ******* ")
        self.driver = Test001Search.driver
        self.sp = SearchPage(self.driver)
        get_product_name = self.sp.getProductName(self.productNumber)
        # print(getProductName)
        self.sp.selectingProduct(self.productNumber)
        time.sleep(5)
        self.cf = CommonFunctions(self.driver)
        self.da = DriverActions(self.driver)
        self.da.child_Window()
        if self.sp.validateProductName(get_product_name):
            self.logger.info("******** Validation of selected product name success ******* ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search.png")
            self.logger.error("******** Selected product name validation failed ******* ")
            assert False

    def test_addToCart(self):
        self.logger.info("******** Adding the product to cart ******* ")
        self.driver = Test001Search.driver
        self.pp = ProductPage(self.driver)
        self.pp.addToCart()
        time.sleep(5)
        if self.pp.validateAddToCart():
            self.logger.info("******** Add to Product is validated ******* ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search.png")
            self.logger.error("******** Validation of add to product is failed ******* ")
            assert False
        self.driver.close()
