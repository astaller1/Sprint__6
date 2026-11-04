import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    options = webdriver.FirefoxOptions()
    
    driver_instance = webdriver.Firefox(options=options)

    driver_instance.maximize_window()

    driver_instance.implicitly_wait(10)

    yield driver_instance

    driver_instance.quit()