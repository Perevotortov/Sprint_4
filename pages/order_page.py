import allure
from .base_page import BasePage
from pages.yandex_page import YandexPage
from locators.order_page_locators import OrderPageLocators, OrderPage2Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    ORDER_PAGE_URL = "https://qa-scooter.praktikum-services.ru/order"

    @allure.step('Открываем страницу заказа')
    def get_order_page(self):
        self.driver.get(self.ORDER_PAGE_URL)
        self.find_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Вводим данные для заказа')
    def enter_order_data(self, name, sec_name, adress, metro, phone, date, comment):
        self.find_element(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_element(OrderPageLocators.SECOND_NAME_FIELD).send_keys(sec_name)
        self.find_element(OrderPageLocators.ADRESS_FIELD).send_keys(adress)
        metro_field = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_field.send_keys(metro)
        metro_list = self.find_element(OrderPageLocators.METRO_LIST)
        metro_list.send_keys(Keys.DOWN)
        metro_list.send_keys(Keys.ENTER)
        phone_field = self.find_element(OrderPageLocators.PHONE_FIELD)
        phone_field.send_keys(phone)
        next_button = self.find_element(OrderPageLocators.BUTTON_NEXT)
        next_button.click()
        date_field = self.find_element(OrderPage2Locators.DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        comment_field = self.find_element(OrderPage2Locators.COMMENT_FIELD)
        comment_field.send_keys(comment)
        rent_time_field = self.find_element(OrderPage2Locators.RENT_TIME_FIELD)
        rent_time_field.click()
        rent_time_value = self.find_element(OrderPage2Locators.RENT_TIME)
        rent_time_value.click()
        color_grey = self.find_element(OrderPage2Locators.COLOR_GREY)
        color_grey.click()
        color_black = self.find_element(OrderPage2Locators.COLOR_BLACK)
        color_black.click()
        order_button = self.find_element(OrderPage2Locators.ORDER_BUTTON)
        order_button.click()

    @allure.step('Нажимаем кнопку "Да"')
    def click_yes_button(self):
        self.click_element(OrderPage2Locators.YES_BUTTON)

    @allure.step('Нажимаем кнопку "Самокат"')
    def click_scooter_button(self):
        self.click_element(OrderPageLocators.BUTTON_SCOOTER)

    @allure.step('Нажимаем кнопку "Яндекс"')
    def click_yandex_button(self):
        self.click_element(OrderPageLocators.BUTTON_YANDEX)

    @allure.step('Проверяем что url новой вкладки соответствует ожидаемому')
    def check_yandex_window(self, locator, timeout=10):
        self.windows_switch()
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(YandexPage.SEARCH_BUTTON))
        return self.url_current() == locator