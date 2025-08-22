from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestGoToConstructorFromAccount:

    def test_redirect_to_constructor_via_constructor_label(self, start_from_login_page, wait):

        driver = start_from_login_page

        # нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.personal_account_button).click()
    
        # подождать загрузки надписи "Конструктор" и нажать на неё
        wait.until(EC.visibility_of_element_located(Locators.constructor_label))
        driver.find_element(*Locators.constructor_label).click()

        # подождать загрузки главной страницы
        wait.until(EC.visibility_of_element_located(Locators.create_burger_title))

        # ждём, что URL изменится на main_page
        wait.until(EC.url_to_be(main_page))

        # проверить, что мы на главной странице
        assert driver.current_url == main_page


    def test_redirect_to_constructor_via_logo(self, start_from_login_page, wait):

        driver = start_from_login_page

        # нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.personal_account_button).click()
    
        # подождать загрузки лого Stellar Burgers и нажать на него
        wait.until(EC.visibility_of_element_located(Locators.stellar_burgers_logo))
        driver.find_element(*Locators.stellar_burgers_logo).click()

        # подождать загрузки главной страницы
        wait.until(EC.visibility_of_element_located(Locators.create_burger_title))

        # ждём, что URL изменится на main_page
        wait.until(EC.url_to_be(main_page))

        # проверить, что мы на главной странице
        assert driver.current_url == main_page