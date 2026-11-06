from selenium.webdriver.common.by import By


class MainScooterLocators:

    @staticmethod
    def get_faq_locator(index):
        return (By.ID, f'accordion__heading-{index}')

    @staticmethod
    def get_faq_answer_locator(index):
        return (By.ID, f'accordion__panel-{index}')

    accept_cookie_button = (By.ID, "rcc-confirm-button")
  
    order_bottom_button = (By.XPATH, '//div[starts-with(@class, "Home_FinishButton")]//button')
    order_header_button = (By.XPATH, '//div[starts-with(@class, "Header_Nav")]//button[text()="Заказать"]')
    home_page_header = (By.XPATH, '//div[contains(@class, "Home_Header")]')
    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]')
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')
 
 