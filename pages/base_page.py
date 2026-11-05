from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import MainScooterLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element_with_wait(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def click_element_with_wait(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def accept_cookies_if_present(self):
        try:
            cookie_button = MainScooterLocators.accept_cookie_button 
            self.wait.until(expected_conditions.visibility_of_element_located(cookie_button)).click()
        except:
            pass

 
 