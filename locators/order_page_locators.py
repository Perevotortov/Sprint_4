from selenium.webdriver.common.by import By

class OrderPageLocators:
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")
    BUTTON_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    BUTTON_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']") #Поле фамилии
    ADRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") #Поле адреса
    METRO_FIELD = (By.XPATH,  "//input[@placeholder='* Станция метро']") #Станция метро
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") #Телефон для курьера
    CURRENT_METRO = (By.XPATH, "//div[@class='select_search select']") #локатор для списка станции метро
    METRO_LIST = (By.CSS_SELECTOR, ".select-search__input")

class OrderPage2Locators:
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Телефон курьера
    RENT_TIME_FIELD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")  # Срок аренды
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") #Комментарий для курьера
    RENT_TIME = (By.XPATH, "//div[contains(text(),'сутки')]")
    COLOR_GREY = (By.XPATH, "//input[@id='grey']")
    COLOR_BLACK = (By.XPATH, "//input[@id='black']")
    ORDER_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM:nth-child(2)") #Кнопка заказа в нижней части страницы заказа
    YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
