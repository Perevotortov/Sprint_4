import allure
import pytest

from locators.order_page_locators import OrderPage2Locators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestScooterOrder:
    @allure.title('Проверка на заполнение страницы заказа самоката')
    @allure.description(
        'Заполняем вторую страницу заказа и оформляем заказ')
    @pytest.mark.parametrize('name, sec_name, address, metro, phone, date, comment', [
        ['Кирилл', 'Провоторов', 'Новая площадь, 10', 'Лубянка', '+79228374542', '07.10.2023', ''],
        ['Андрей', 'Пароваров', 'Старая площадь, 4', 'Китай-город', '+79228374542', '12.07.2024',
         'Позвоните за 15 минут']
    ])
    def test_order_scooter(self, driver, name, sec_name, address, metro, phone, date, comment):
        order_page = OrderPage(driver)
        order_page.get_order_page()
        order_page.enter_order_data(name, sec_name, address, metro, phone, date, comment)
        order_page.click_yes_button()
        assert order_page.check_element_displayed(OrderPage2Locators.STATUS_BUTTON), f"Некорректный ОР заказа. Ожидалось отображение кнопки статуса заказа"

    @allure.title('Проверка на переход к странице заказа через кнопку в хедере')
    @allure.description('На главной странице нажимаем на кнопку "Заказать" и проверяем, что осуществлен переход на страницу заказа')
    def test_top_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        assert order_page.url_current() == order_page.ORDER_PAGE_URL, f"Некорректный URL страницы. Ожидалось: {order_page.ORDER_PAGE_URL}"

    @allure.title('Проверка на переход к странице заказа через кнопку заказа в блоке "как это работает?"')
    @allure.description(
        'На главной странице нажимаем на кнопку "Заказать" в блоке "как это работает?" и проверяем, что осуществлен переход на страницу заказа')
    def test_second_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_second_order_button()
        order_page = OrderPage(driver)
        assert order_page.url_current() == order_page.ORDER_PAGE_URL, f"Некорректный URL страницы. Ожидалось: {order_page.ORDER_PAGE_URL}"