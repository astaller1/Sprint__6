from locators.base_page_locators import MainScooterLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainScooterPage:

    def __init__(self, driver):
        self.driver = driver


    def click_question(self, index):

        locator = MainScooterLocators.get_faq_locator(index)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator)).click()

    def get_answer_text(self, index):

        locator = MainScooterLocators.get_faq_answer_locator(index)

        return self.driver.find_element(*locator).text

    def accept_cookies_if_present(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(MainScooterPage.accept_cookie_button)).click()
        except:
            pass
 
 