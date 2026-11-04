from selenium.webdriver.common.by import By


class OrderScooterLocators:

    name_input = [By.XPATH, '//input[@placeholder="* Имя"]']
    surname_input = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    station_input = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    @staticmethod
    def get_station_option_locator(station_name):
        return (By.XPATH, f'//li[@class="select-search__row"]//*[text()="{station_name}"]')
    
    phone_input = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, '//button[text()="Далее"]']

    date_input = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    rent_time_dropdown = [By.XPATH, '//div[@class="Dropdown-placeholder"]']
    rent_time_input_option_one_day = [By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]']
    rent_time_input_option_two_days = [By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]']
    color_black_checkbox = [By.ID, 'black']
    color_grey_checkbox = [By.ID, 'grey']
    comment_input = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    final_order_button = [By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]']

    confirm_button = [By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Да"]']
    success_order_modal = [By.XPATH, '//div[contains(@class, "Order_ModalHeader") and text()="Заказ оформлен"]']
    status_button = [By.XPATH, '//div[contains(@class, "Order_NextButton")]/button']
 