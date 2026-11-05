from selenium.webdriver.common.by import By


class MainScooterLocators:

    @staticmethod
    def get_faq_locator(index):
        return (By.ID, f'accordion__heading-{index}')

    @staticmethod
    def get_faq_answer_locator(index):
        return (By.ID, f'accordion__panel-{index}')

    accept_cookie_button = (By.ID, "rcc-confirm-button")
  
    order_bottom_button = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]//button')
    order_header_button = (By.XPATH, '//div[contains(@class, "Header_Nav")]//button[text()="Заказать"]')
    scooter_logo = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    yandex_logo = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')
    home_page_header = (By.XPATH, '//div[contains(@class, "Home_Header")]')
 
 
