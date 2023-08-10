import allure
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestQuestionsOnMainPage:
    @allure.title('Проверка "Сколько это стоит?"')
    @allure.description('На странице ищем первый вопрос и проверяем отображение ответа на вопрос')
    def test_cost_question(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION1)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT1))
        element = driver.find_element(*MainPage.TEXT1)
        assert element.is_displayed()


    @allure.title('Проверка "Хочу сразу несколько самокатов!"')
    @allure.description('На странице ищем второй вопрос и проверяем отображение ответа на вопрос')
    def test_several_scooters(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION2)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT2))
        element = driver.find_element(*MainPage.TEXT2)
        assert element.is_displayed()


    @allure.title('Проверка "Как рассчитывается время аренды?"')
    @allure.description('На странице ищем третий вопрос и проверяем отображение ответа на вопрос')
    def test_rent_time(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION3)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT3))
        element = driver.find_element(*MainPage.TEXT3)
        assert element.is_displayed()

    @allure.title('Проверка "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('На странице ищем четвертый вопрос и проверяем отображение ответа на вопрос')
    def test_scooter_today(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION4)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT4))
        element = driver.find_element(*MainPage.TEXT4)
        assert element.is_displayed()

    @allure.title('Проверка "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('На странице ищем пятый вопрос и проверяем отображение ответа на вопрос')
    def test_scooter_extend_or_return(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION5)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT5))
        element = driver.find_element(*MainPage.TEXT5)
        assert element.is_displayed()


    @allure.title('Проверка "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('На странице ищем шестой вопрос и проверяем отображение ответа на вопрос')
    def test_charge_station(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION6)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT6))
        element = driver.find_element(*MainPage.TEXT6)
        assert element.is_displayed()


    @allure.title('Проверка "Можно ли отменить заказ?"')
    @allure.description('На странице ищем седьмой вопрос и проверяем отображение ответа на вопрос')
    def test_order_cancel(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION7)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT7))
        element = driver.find_element(*MainPage.TEXT7)
        assert element.is_displayed()


    @allure.title('Проверка "Я жизу за МКАДом, привезёте?"')
    @allure.description('На странице ищем восьмой вопрос и проверяем отображение ответа на вопрос')
    def test_beyond_mkad(self, questions_scroll):
        driver = questions_scroll
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.QUESTION8)).click()
        wait.until(EC.visibility_of_element_located(MainPage.TEXT8))
        element = driver.find_element(*MainPage.TEXT8)
        assert element.is_displayed()