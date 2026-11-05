from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from locators.base_page_locators import MainScooterLocators
import time

class MainScooterPage(BasePage):

    def click_question(self, index):
        locator = MainScooterLocators.get_faq_locator(index)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.click_element_with_wait(locator)

    def get_answer_text(self, index):
        locator = MainScooterLocators.get_faq_answer_locator(index)
        return self.find_element_with_wait(locator).text

    def click_order_header_button(self):
        self.accept_cookies_if_present()
        self.click_element_with_wait(MainScooterLocators.order_header_button)

    def click_order_bottom_button(self):
        self.accept_cookies_if_present()
        button = self.wait.until(expected_conditions.presence_of_element_located(MainScooterLocators.order_bottom_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.click_element_with_wait(MainScooterLocators.order_bottom_button)

    def click_scooter_logo(self):
        self.click_element_with_wait(MainScooterLocators.scooter_logo)

    def click_yandex_logo(self):
        self.click_element_with_wait(MainScooterLocators.yandex_logo)

    def is_main_page_open(self):
        return self.find_element_with_wait(MainScooterLocators.home_page_header).is_displayed()
