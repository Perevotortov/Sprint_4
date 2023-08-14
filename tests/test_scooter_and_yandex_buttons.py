import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.yandex_page import YandexPage


class TestButtons:
    @allure.title('Проверка на переход к главной странцие при нажатии на Самокат')
    @allure.description(
        'Нажимаем на Самокат, проверяем что совершен переход на главную страницу')
    def test_click_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.get_order_page()
        order_page.click_scooter_button()
        main_page = MainPage(order_page)
        assert order_page.url_current() == main_page.MAIN_PAGE_URL, f"Некорректный URL страницы. Ожидалось: {main_page.MAIN_PAGE_URL}"

    @allure.title('Проверка на переход к главной странцие Яндекса')
    @allure.description(
        'Нажимаем на Яндекс и переходим на главную страницу в новой вкладке, ждем появления кнопки Найти и проверяем current url')
    def test_click_yandex(self, driver):
        order_page = OrderPage(driver)
        order_page.get_order_page()
        order_page.click_yandex_button()
        assert order_page.check_yandex_window(YandexPage.YANDEX_URL), f"Некорректный URL страницы. Ожидалось: {YandexPage.YANDEX_URL}"