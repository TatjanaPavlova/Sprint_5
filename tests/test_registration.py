from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import *
from locators import Locators
from curl import *


class TestNewUserRegistration:

    def test_successful_registration(self, driver, wait):

        # открыть страницу регистрации
        driver.get(login_page)
        driver.find_element(*Locators.registration_button).click()

        # заполнить поля
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.name_field).send_keys(name)
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
    
        # нажать на кнопку "Зарегистрироваться" и перейти на страницу авторизации
        wait.until(EC.element_to_be_clickable(Locators.complete_registration_button)).click()
        wait.until(EC.visibility_of_element_located(Locators.entrance_label))

        # заполнить поля данными, указанными при регистрации
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.entrance_button).click()
        
        # проверить, что мы на главной странице
        wait.until(EC.visibility_of_element_located(Locators.create_burger_title))
        wait.until(EC.url_to_be(main_page))
        assert driver.current_url == main_page


    def test_registration_with_short_password_fails(self, driver, wait):

        # зайти на страницу регистрации
        driver.get(login_page)
        driver.find_element(*Locators.registration_button).click()

        # заполнить поля и нажать на кнопку "Зарегистрироваться"
        name, email, short_password = generate_registration_data_with_short_password()
        driver.find_element(*Locators.name_field).send_keys(name)
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(short_password)
        driver.find_element(*Locators.complete_registration_button).click()

        # проверить, что появилась надпись "Некорректный пароль"
        error_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.incorrect_password_label))
        assert "Некорректный пароль" in error_element.text
