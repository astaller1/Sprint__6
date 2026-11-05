import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.main_page import MainScooterPage
from pages.order_page import OrderScooterPage
from data import OrderInputData


@pytest.mark.parametrize('entry_point, name, surname, address, station_name, phone, date, period, color, comment', OrderInputData.full_data_set)
def test_order_full_flow(driver, entry_point, name, surname, address, station_name, phone, date, period, color, comment):
    
    driver.get('https://qa-scooter.praktikum-services.ru/')

    main_page = MainScooterPage(driver)
    order_page = OrderScooterPage(driver)


    if entry_point == 'header':
        main_page.click_order_header_button()
    else:
        main_page.click_order_bottom_button()
  

    order_page.fill_personal_data(name, surname, address, station_name, phone)
    order_page.fill_rent_data(date, period, color, comment)

    assert order_page.is_success_modal_visible()

    order_page.close_modal()

    main_page.click_scooter_logo()
    assert main_page.is_main_page_open()

    current_window = driver.window_handles
    main_page.click_yandex_logo()
    main_page.wait.until(expected_conditions.new_window_is_opened(current_window))

    for window_handle in driver.window_handles:
        if window_handle not in current_window:
            driver.switch_to.window(window_handle)
            break

    main_page.wait.until(expected_conditions.url_contains('dzen.ru'))
    assert 'dzen.ru' in driver.current_url
 
