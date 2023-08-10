import allure
import pytest
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage, OrderPage2, YandexPage


class TestScooterOrder:
    @allure.title('Проверка на переход к странице заказа через кнопку справа в верху')
    @allure.description('На главной странице нажимаем на кнопку "Заказать" и проверяем, что осуществлен переход на страницу заказа')
    def test_top_order_button(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.find_element(*MainPage.TOP_ORDER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(OrderPage.BUTTON_NEXT))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"


    @allure.title('Проверка на переход к странице заказа через кнопку заказа в блоке "как это работает?"')
    @allure.description(
        'На главной странице нажимаем на кнопку "Заказать" в блоке "как это работает?" и проверяем, что осуществлен переход на страницу заказа')
    def test_second_order_button(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.find_element(*MainPage.COOKIE_WARNING).click()
        driver.find_element(*MainPage.SECOND_ODRER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(OrderPage.BUTTON_NEXT))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"


    @allure.title('Проверка на переход к главной странцие при нажатии на Самокат')
    @allure.description(
        'Нажимаем на Самокат на странице заказа, проверяем что совершен переход на главную страницу')
    def test_click_logo(self, driver_order_page):
        driver = driver_order_page
        driver.find_element(*OrderPage.BUTTON_SCOOTER).click()
        assert driver.find_element(*MainPage.TOP_ORDER_BUTTON).is_displayed()


    @allure.title('Проверка на переход к главной странцие Яндекса')
    @allure.description(
        'Нажимаем на Яндекс и переходим на главную страницу в новой вкладке, ждем появления кнопки Найти и проверяем current url')
    def test_click_yandex(self, driver_order_page):
        driver = driver_order_page
        main_window = driver.current_window_handle
        driver.find_element(*OrderPage.BUTTON_YANDEX).click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.number_of_windows_to_be(2))
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)
        wait.until(EC.visibility_of_element_located(YandexPage.SEARCH_BUTTON))
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'


    @allure.title('Проверка на заполнение первой страницы заказа')
    @allure.description(
        'Открываем страницу заказа и вводим тестовые данные, нажимаем Далее, проверям что страница изменилась на вторую')
    @pytest.mark.parametrize('name, sec_name, adress, metro, phone',
    [['Кирилл', 'Провоторов', 'Новая площадь, 10', 'Лубянка', '+79228374542'], ['Андрей', 'Пароваров', 'Старая площадь, 4', 'Китай-город', '+79228374542']])
    def test_order_first_page(self, enter_data_order):
        driver = enter_data_order
        driver.find_element(*OrderPage.BUTTON_NEXT).click()
        assert driver.find_element(*OrderPage2.ORDER_BUTTON).is_displayed()


    @allure.title('Проверка на заполнение второй страницы заказа')
    @allure.description(
        'Заполняем вторую страницу заказа и оформляем заказ')
    @pytest.mark.parametrize('name, sec_name, adress, metro, phone, date, comment',
    [['Кирилл', 'Провоторов', 'Новая площадь, 10', 'Лубянка', '+79228374542', '07.10.2023', ''],
    ['Андрей', 'Пароваров', 'Старая площадь, 4', 'Китай-город', '+79228374542', '12.07.2024', 'Позвоните за 15 минут']])
    def test_order_second_page(self, enter_data_order, date, comment):
        driver = enter_data_order
        wait = WebDriverWait(driver, 5)
        driver.find_element(*OrderPage.BUTTON_NEXT).click()
        driver.find_element(*OrderPage2.DATE_FIELD).send_keys(date)
        driver.find_element(*OrderPage2.DATE_FIELD).send_keys(Keys.ENTER)
        driver.find_element(*OrderPage2.COMMENT_FIELD).send_keys(comment)
        driver.find_element(*OrderPage2.RENT_TIME_FIELD).click()
        driver.find_element(*OrderPage2.RENT_TIME).click()
        driver.find_element(*OrderPage2.COLOR_GREY).click()
        driver.find_element(*OrderPage2.COLOR_BLACK).click()
        driver.find_element(*OrderPage2.ORDER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(OrderPage2.YES_BUTTON)).click()
        assert driver.find_element(*OrderPage2.STATUS_BUTTON).is_displayed()