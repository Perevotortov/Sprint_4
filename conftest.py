import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
from pages.order_page import OrderPage



@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('https://qa-scooter.praktikum-services.ru/')
    yield browser
    browser.quit()

@pytest.fixture
def questions_scroll(driver):
    button = driver.find_element(*MainPage.QUESTION1)
    driver.execute_script("arguments[0].scrollIntoView();", button)
    return driver

@pytest.fixture
def driver_order_page(driver):
    wait = WebDriverWait(driver, 3)
    driver.find_element(*MainPage.TOP_ORDER_BUTTON).click()
    wait.until(EC.visibility_of_element_located(OrderPage.BUTTON_NEXT))
    return driver

@pytest.fixture
def enter_data_order(driver_order_page, name, sec_name, adress, metro, phone):
        driver = driver_order_page
        driver.find_element(*OrderPage.NAME_FIELD).send_keys(name)
        driver.find_element(*OrderPage.SECOND_NAME_FIELD).send_keys(sec_name)
        driver.find_element(*OrderPage.ADRESS_FIELD).send_keys(adress)
        driver.find_element(*OrderPage.METRO_FIELD).send_keys(metro)
        driver.find_element(*OrderPage.METRO_LIST).send_keys(Keys.DOWN)
        driver.find_element(*OrderPage.METRO_LIST).send_keys(Keys.ENTER)
        driver.find_element(*OrderPage.PHONE_FIELD).send_keys(phone)
        return driver
