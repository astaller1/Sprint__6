from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderScooterLocators
import allure

class OrderScooterPage(BasePage):

    @allure.step('Заполнить первую форму оформления заказа: имя "{name}", фамилия "{surname}", адрес "{address}", станция метро "{station_name}", номер телефона "{phone}"')
    def fill_personal_data(self, name, surname, address, station_name, phone):
        self.enter_text(OrderScooterLocators.name_input, name)
        self.enter_text(OrderScooterLocators.surname_input, surname)
        self.enter_text(OrderScooterLocators.address_input, address)

        self.click_element_with_wait(OrderScooterLocators.station_input)
        self.enter_text(OrderScooterLocators.station_input, station_name)
        station_option = OrderScooterLocators.get_station_option_locator(station_name)
        self.click_element_with_wait(station_option)

        self.enter_text(OrderScooterLocators.phone_input, phone)
        self.click_element_with_wait(OrderScooterLocators.next_button)

    @allure.step('Заполнить вторую форму оформления заказа: дата "{date}", срок аренды "{period}", цвет "{color}", комментарий "{comment}"')
    def fill_rent_data(self, date, period, color, comment):
        date_window = self.find_element_with_wait(OrderScooterLocators.date_input)
        date_window.send_keys(date)
        date_window.send_keys(Keys.ENTER)

        self.click_element_with_wait(OrderScooterLocators.rent_time_dropdown)
        if period == 'сутки':
            self.click_element_with_wait(OrderScooterLocators.rent_time_input_option_one_day)
        else:
            self.click_element_with_wait(OrderScooterLocators.rent_time_input_option_two_days)

        if color == 'black':
            self.click_element_with_wait(OrderScooterLocators.color_black_checkbox)
        elif color == 'grey':
            self.click_element_with_wait(OrderScooterLocators.color_grey_checkbox)

        if comment:
            self.enter_text(OrderScooterLocators.comment_input, comment)

        self.click_element_with_wait(OrderScooterLocators.final_order_button)
        self.click_element_with_wait(OrderScooterLocators.confirm_button)

    @allure.step('Проверить, что появилось окно успешного оформления заказа')
    def is_success_modal_visible(self):
        return self.find_element_with_wait(OrderScooterLocators.success_order_modal).is_displayed()
 