import pytest 
from pages.main_page import MainScooterPage
from data import TestData
import allure

@allure.title('Проверка соответствия ответа на вопрос №{index} в блоке FAQ')
@pytest.mark.parametrize('index, expected_text', enumerate(TestData.FAQ_answers))
def test_faq_answer_connects_to_its_question(driver, index, expected_text):

    page = MainScooterPage(driver)

    page.open_url(TestData.Main_page_url)
    page.accept_cookies_if_present()
    page.click_question(index)
    actual_text = page.get_answer_text(index)

    assert actual_text == expected_text
 