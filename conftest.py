import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators
from data import Credentials


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.email_field).send_keys(Credentials.email)   # Ввести email
    driver.find_element(*Locators.password_field).send_keys(Credentials.password)  # Ввести пароль
    driver.find_element(*Locators.entrance_button).click()  # Нажать на кнопку "Войти"

    return driver


@pytest.fixture 
def start_from_login_page(driver):  # Вход с главной страницы
    driver.get(main_page)

    driver.find_element(*Locators.log_in_to_account_button).click()  # Нажать на кнопку "Войти в аккаунт"   
    driver.find_element(*Locators.email_field).send_keys(Credentials.email)   # Ввести email
    driver.find_element(*Locators.password_field).send_keys(Credentials.password)  # Ввести пароль
    driver.find_element(*Locators.entrance_button).click()  # Нажать на кнопку "Войти"

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.create_burger_title))

    return driver


@pytest.fixture
def wait(driver):
    """Фикстура для явных ожиданий"""
    return WebDriverWait(driver, 10)