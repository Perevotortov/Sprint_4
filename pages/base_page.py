import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Кликаем по элементу')
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        return element

    @allure.step('Получаем текущий URL страницы')
    def url_current(self):
        return self.driver.current_url