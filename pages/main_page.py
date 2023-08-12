import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    TRUE_TEXT1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    TRUE_TEXT2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    TRUE_TEXT3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    TRUE_TEXT4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    TRUE_TEXT5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    TRUE_TEXT6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    TRUE_TEXT7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    TRUE_TEXT8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Проматываем страницу до раздела с вопросами')
    def scroll_to_question(self, locator):
        button = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Нажимаем вопрос')
    def click_question(self, locator):
        self.click_element(locator)

    @allure.step('Проверяем отображение ответа')
    def check_answer(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step('Получаем ответ на вопрос после нажатия на него')
    def get_question_answer(self, question_locator, answer_locator):
        self.scroll_to_question(question_locator)
        self.click_question(question_locator)
        answer = self.check_answer(answer_locator)
        return (question_locator, answer)

    @allure.step('Нажимаем на кнопку "Заказать" в хедере страницы')
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку "Заказать" в блоке "Как это работает?"')
    def click_second_order_button(self):
        self.click_element(MainPageLocators.COOKIE_WARNING)
        self.click_element(MainPageLocators.SECOND_ODRER_BUTTON)