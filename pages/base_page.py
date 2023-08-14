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

    @allure.step('Проматываем страницу до раздела с вопросами')
    def scroll_to_question(self, locator):
        button = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Проверяем отображение элемента на странице')
    def check_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step('Проверяем что количество окон стало 2, и переключаемся на новую вкладку')
    def windows_switch(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text