from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_WARNING = (By.XPATH, "//button[@id='rcc-confirm-button']") #Кнопка для куков
    QUESTION1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    TEXT1 = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей')]")
    QUESTION2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    TEXT2 = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат')]")
    QUESTION3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    TEXT3 = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая')]")
    QUESTION4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    TEXT4 = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня')]")
    QUESTION5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    TEXT5 = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное')]")
    QUESTION6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    TEXT6 = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой')]")
    QUESTION7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    TEXT7 = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли')]")
    QUESTION8 = (By.XPATH, "//div[@id='accordion__heading-7']")
    TEXT8 = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов!')]")
    TOP_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать')]") #Кнопка для заказа в хедере
    SECOND_ODRER_BUTTON = (By.XPATH, "//div[5]/button") #Кнопка для заказа в блоке "как это работает?"