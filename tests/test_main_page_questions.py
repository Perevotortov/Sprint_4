import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestQuestionsOnMainPage:
    @allure.title('Проверка вопросов на главной странице')
    @allure.description(
        'Проверяем что при нажатии на каждый вопрос появляется соответствующий ответ')
    @pytest.mark.parametrize("question_locator, answer_locator, true_text", [
        (MainPageLocators.QUESTION1, MainPageLocators.TEXT1, MainPage.TRUE_TEXT1),
        (MainPageLocators.QUESTION2, MainPageLocators.TEXT2, MainPage.TRUE_TEXT2),
        (MainPageLocators.QUESTION3, MainPageLocators.TEXT3, MainPage.TRUE_TEXT3),
        (MainPageLocators.QUESTION4, MainPageLocators.TEXT4, MainPage.TRUE_TEXT4),
        (MainPageLocators.QUESTION5, MainPageLocators.TEXT5, MainPage.TRUE_TEXT5),
        (MainPageLocators.QUESTION6, MainPageLocators.TEXT6, MainPage.TRUE_TEXT6),
        (MainPageLocators.QUESTION7, MainPageLocators.TEXT7, MainPage.TRUE_TEXT7),
        (MainPageLocators.QUESTION8, MainPageLocators.TEXT8, MainPage.TRUE_TEXT8)
    ])
    def test_question_answer(self, driver, question_locator, answer_locator, true_text):
        main_page = MainPage(driver)
        main_page.get_question_answer(question_locator, answer_locator)
        assert main_page.find_element(answer_locator).text == true_text