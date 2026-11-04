from locators.base_page_locators import MainScooterLocators
from locators.order_page_locators import OrderScooterLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def accept_cookies_if_present(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(MainScooterPage.accept_cookie_button)).click()
        except:
            pass

class MainScooterPage(BasePage):

    def click_order_header_button(self):
        self.accept_cookies_if_present()
        self.wait.until(expected_conditions.element_to_be_clickable(MainScooterLocators.order_header_button)).click()

    def click_order_bottom_button(self):
        self.accept_cookies_if_present()
        button = self.wait.until(expected_conditions.presence_of_element_located(MainScooterLocators.order_bottom_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.wait.until(expected_conditions.element_to_be_clickable(MainScooterLocators.order_bottom_button)).click()

    def click_scooter_logo(self):
        self.wait.until(expected_conditions.visibility_of_element_located(MainScooterLocators.scooter_logo)).click()

    def click_yandex_logo(self):
        self.wait.until(expected_conditions.visibility_of_element_located(MainScooterLocators.yandex_logo)).click()

    def is_main_page_open(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(MainScooterLocators.home_page_header)).is_displayed()


class OrderScooterPage(BasePage):

    def fill_personal_data(self, name, surname, address, station_name, phone):
        self.wait.until(expected_conditions.visibility_of_element_located(OrderScooterLocators.name_input)).send_keys(name)
        self.driver.find_element(*OrderScooterLocators.surname_input).send_keys(surname)
        self.driver.find_element(*OrderScooterLocators.address_input).send_keys(address)

        metro_station = self.driver.find_element(*OrderScooterLocators.station_input)
        metro_station.click()
        metro_station.send_keys(Keys.DOWN)
        for letter in station_name:
            metro_station.send_keys(letter)
            time.sleep(0.1)

        station_option = OrderScooterLocators.get_station_option_locator(station_name)
        self.wait.until(expected_conditions.visibility_of_element_located(station_option)).click()

        self.driver.find_element(*OrderScooterLocators.phone_input).send_keys(phone)
        self.driver.find_element(*OrderScooterLocators.next_button).click()

    def fill_rent_data(self, date, period, color, comment):
        date_window = self.wait.until(expected_conditions.visibility_of_element_located(OrderScooterLocators.date_input))
        date_window.send_keys(date)
        date_window.send_keys(Keys.ENTER)

        self.driver.find_element(*OrderScooterLocators.rent_time_dropdown).click()
        if period == 'сутки':
            self.wait.until(expected_conditions.element_to_be_clickable(OrderScooterLocators.rent_time_input_option_one_day)).click()
        else:
            self.wait.until(expected_conditions.element_to_be_clickable(OrderScooterLocators.rent_time_input_option_two_days)).click()

        if color == 'black':
            self.driver.find_element(*OrderScooterLocators.color_black_checkbox).click()
        elif color == 'grey':
            self.driver.find_element(*OrderScooterLocators.color_grey_checkbox).click()

        if comment:
            self.driver.find_element(*OrderScooterLocators.comment_input).send_keys(comment)
        self.driver.find_element(*OrderScooterLocators.final_order_button).click()
        self.wait.until(expected_conditions.element_to_be_clickable(OrderScooterLocators.confirm_button)).click()

    def is_success_modal_visible(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(OrderScooterLocators.success_order_modal)).is_displayed()

    def close_modal(self):
        self.driver.find_element(*OrderScooterLocators.status_button).click()
    
 