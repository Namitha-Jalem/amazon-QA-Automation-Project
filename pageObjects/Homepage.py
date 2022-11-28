from pageObjects.DriverActions import DriverActions
from selenium.webdriver.common.by import By


class Homepage(DriverActions):
    # Object repositories or webelements locator are related to homepage are stored here
    textbox_search_id = "twotabsearchtextbox"
    button_search_xpath = "//*[@id='nav-search-submit-button']"
    dropdown_search_id = "searchDropdownBox"
    by_locator_btn = (By.XPATH, button_search_xpath)
    by_locator_search_txt = (By.ID, textbox_search_id)

    def __init__(self, driver):
        super().__init__(driver)

    def setSearchText(self, search_text):       # Performing the search action
        self.driver.find_element("id", self.textbox_search_id).clear()
        self.send_values(self.by_locator_search_txt, search_text)
        self.click_button(self.by_locator_btn)
