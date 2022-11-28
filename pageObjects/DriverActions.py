from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Just to demonstrate the reusable functions for driver actions created these methods,
# but list can be more extensive & optimized.

class DriverActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def click_button(self, by_locator):  # Performs click action
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def click_element_list(self, by_locator, prod_num):  # performs the click action on the list of webelements
        element = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        element[prod_num].click()

    def send_values(self, by_locator, text):  # send the value to the textbox
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    def child_Window(self):  # switch to child window (can be enhanced later)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
