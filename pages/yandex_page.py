from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class YandexPage(BasePage):
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Найти')]")
    YANDEX_URL = 'https://dzen.ru/?yredirect=true'