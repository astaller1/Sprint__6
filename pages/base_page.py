from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainScooterLocators
import allure
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Ожидание отображения элемента на странице')
    def find_element_with_wait(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности и клик по элементу')
    def click_element_with_wait(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Принять куки(если отображаются)')
    def accept_cookies_if_present(self):
        try:
            cookie_button = MainScooterLocators.accept_cookie_button 
            self.wait.until(expected_conditions.visibility_of_element_located(cookie_button)).click()
        except:
            pass

    @allure.step('Прокрутить до низа страницы')
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        button = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

    @allure.step('Ввести текст "{text}" в элемент')
    def enter_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Открыть страницу по URL: {url}')
    def open_url(self,url):
        self.driver.get(url)

    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_element_with_wait(MainScooterLocators.scooter_logo)

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_element_with_wait(MainScooterLocators.yandex_logo)

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self):

        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

        time.sleep(3)

        return self.driver.current_url
 