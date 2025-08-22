from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestCheckEntrance:

    def test_login_via_main_page_login_button(self, driver, wait):

        # открыть главную страницу
        driver.get(main_page)

        # нажать на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.log_in_to_account_button).click()
    
        # подождать загрузки надписи "Вход"
        wait.until(EC.visibility_of_element_located(Locators.entrance_label))

        # ждём, что URL изменится на login_page
        wait.until(EC.url_to_be(login_page))

        # проверить, что мы на странице авторизации
        assert driver.current_url == login_page


    def test_login_via_personal_cabinet_button(self, driver, wait):

        # открыть главную страницу
        driver.get(main_page)

        # нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.personal_account_button).click()
    
        # подождать загрузки надписи "Вход"
        wait.until(EC.visibility_of_element_located(Locators.entrance_label))

        # ждём, что URL изменится на login_page
        wait.until(EC.url_to_be(login_page))

        # проверить, что мы на странице авторизации
        assert driver.current_url == login_page


    def test_login_via_registration_form_login_button(self, driver, wait):

        # открыть страницу регистрации
        driver.get(register_page)

        # нажать на кнопку "Войти"
        driver.find_element(*Locators.login_button_registration_or_recovery).click()
    
        # подождать загрузки надписи "Вход"
        wait.until(EC.visibility_of_element_located(Locators.entrance_label))

        # ждём, что URL изменится на login_page
        wait.until(EC.url_to_be(login_page))

        # проверить, что мы на странице авторизации
        assert driver.current_url == login_page


    def test_login_via_password_reset_form_login_button(self, driver, wait):

        # открыть страницу авторизации
        driver.get(login_page)

        # нажать на кнопку "Восстановить пароль"
        driver.find_element(*Locators.password_recovery_button).click()
    
        # подождать загрузки надписи "Восстановление пароля"
        wait.until(EC.visibility_of_element_located(Locators.password_recovery_label))

        # нажать на кнопку "Войти" в форме восстановления пароля
        driver.find_element(*Locators.login_button_registration_or_recovery).click()

        # подождать загрузки надписи "Вход"
        wait.until(EC.visibility_of_element_located(Locators.entrance_label))

        # ждём, что URL изменится на login_page
        wait.until(EC.url_to_be(login_page))

        # проверить, что мы на странице авторизации
        assert driver.current_url == login_page