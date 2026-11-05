import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from locators.order_page_locators import OrderScooterLocators

class OrderScooterPage(BasePage):

    def fill_personal_data(self, name, surname, address, station_name, phone):
        time.sleep(5)
        self.find_element_with_wait(OrderScooterLocators.name_input).send_keys(name)
        self.driver.find_element(*OrderScooterLocators.surname_input).send_keys(surname)
        self.driver.find_element(*OrderScooterLocators.address_input).send_keys(address)

        metro_station = self.driver.find_element(*OrderScooterLocators.station_input)
        metro_station.click()
        metro_station.send_keys(station_name)
        time.sleep(1)


        station_option = OrderScooterLocators.get_station_option_locator(station_name)
        self.find_element_with_wait(station_option).click()

        self.driver.find_element(*OrderScooterLocators.phone_input).send_keys(phone)
        self.driver.find_element(*OrderScooterLocators.next_button).click()

    def fill_rent_data(self, date, period, color, comment):
        date_window = self.find_element_with_wait(OrderScooterLocators.date_input)
        date_window.send_keys(date)
        date_window.send_keys(Keys.ENTER)

        self.driver.find_element(*OrderScooterLocators.rent_time_dropdown).click()
        if period == 'сутки':
            self.click_element_with_wait(OrderScooterLocators.rent_time_input_option_one_day)
        else:
            self.click_element_with_wait(OrderScooterLocators.rent_time_input_option_two_days)

        if color == 'black':
            self.driver.find_element(*OrderScooterLocators.color_black_checkbox).click()
        elif color == 'grey':
            self.driver.find_element(*OrderScooterLocators.color_grey_checkbox).click()

        if comment:
            self.driver.find_element(*OrderScooterLocators.comment_input).send_keys(comment)
        self.driver.find_element(*OrderScooterLocators.final_order_button).click()
        self.click_element_with_wait(OrderScooterLocators.confirm_button)

    def is_success_modal_visible(self):
        return self.find_element_with_wait(OrderScooterLocators.success_order_modal).is_displayed()

    def close_modal(self):
        self.driver.find_element(*OrderScooterLocators.status_button).click()

    
 