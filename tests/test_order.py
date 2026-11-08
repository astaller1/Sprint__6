import pytest
from pages.main_page import MainScooterPage
from pages.order_page import OrderScooterPage
from data import TestData
import allure


@allure.feature('Оформление заказа самоката')
class TestOrderScooter:

    @allure.title('Полный позитивный сценарий оформления заказа через точку входа: {entry_point}')
    @pytest.mark.parametrize('entry_point, name, surname, address, station_name, phone, date, period, color, comment', TestData.full_data_set)
    def test_order_full_flow(self, driver, entry_point, name, surname, address, station_name, phone, date, period, color, comment):

        main_page = MainScooterPage(driver)
        order_page = OrderScooterPage(driver)

        main_page.open_url(TestData.Main_page_url)

        entry_points = {'header': main_page.click_order_header_button, 'bottom': main_page.click_order_bottom_button}

        entry_points[entry_point]()  

        order_page.fill_personal_data(name, surname, address, station_name, phone)
        order_page.fill_rent_data(date, period, color, comment)

        assert order_page.is_success_modal_visible()

@allure.feature('Переходы по логотипам в шапке')
class TestLogoRedirect:

    @allure.title('Клик по логотипу "Самокат" ведет на главную страницу')
    def test_click_scooter_logo_leads_to_main_page(self, driver):

        order_page = OrderScooterPage(driver)
        
        order_page.open_url(TestData.Order_page_url)
        order_page.click_scooter_logo()

        page = MainScooterPage(driver)

        assert page.is_main_page_open()

    @allure.title('Клик по логотипу "Яндекс" ведет на "Яндекс.Дзен"')
    def test_click_yandex_logo_opens_zen(self, driver):

        order_page = OrderScooterPage(driver)

        order_page.open_url(TestData.Order_page_url)

        order_page.click_yandex_logo()

        current_url = order_page.switch_to_new_tab()

        assert 'dzen.ru' in current_url
    