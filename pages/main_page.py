from pages.base_page import BasePage
from locators.main_page_locators import MainScooterLocators
import time
import allure

class MainScooterPage(BasePage):

    @allure.step('Прокрутить страницу вниз и нажать на вопрос №{index} в FAQ')
    def click_question(self, index):
        locator = MainScooterLocators.get_faq_locator(index)
        self.scroll_to_bottom()
        time.sleep(1)
        self.click_element_with_wait(locator)

    @allure.step('Получить текст ответа для вопроса №{index} в FAQ')
    def get_answer_text(self, index):
        locator = MainScooterLocators.get_faq_answer_locator(index)
        return self.find_element_with_wait(locator).text

    @allure.step('Нажать на кнопку "Заказать" в хэдере')
    def click_order_header_button(self):
        self.accept_cookies_if_present()
        self.click_element_with_wait(MainScooterLocators.order_header_button)

    @allure.step('Прокрутить вниз и нажать на большую кнопку "Заказать"')
    def click_order_bottom_button(self):
        self.accept_cookies_if_present()
        self.scroll_to_element(MainScooterLocators.order_bottom_button)
        self.click_element_with_wait(MainScooterLocators.order_bottom_button)

    @allure.step('Проверить, что открыта главная страница')    
    def is_main_page_open(self):
        return self.find_element_with_wait(MainScooterLocators.home_page_header).is_displayed()
 