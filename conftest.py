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

    return driver


@pytest.fixture
def start_from_recovery_page(driver): # Вход со страницы восстановления пароля
    driver.get(login_page)

    # Кликнуть на кнопку "Восстановить пароль"
    driver.find_element(*Locators.password_recovery_button).click()

    # Подождать загрузки кнопки "Войти"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.entrance_button_on_recovery_page))

    # Нажать на кнопку "Войти"
    driver.find_element(*Locators.entrance_button_on_recovery_page).click()

    # Пройти авторизацию
    driver.find_element(*Locators.email_field).send_keys(Credentials.email)   # Ввести email
    driver.find_element(*Locators.password_field).send_keys(Credentials.password)  # Ввести пароль
    driver.find_element(*Locators.entrance_button).click()  # Нажать на кнопку "Войти"
    
    return driver