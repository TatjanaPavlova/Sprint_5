from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestExitFromAccount:

    def test_exit_via_exit_button(self, start_from_login_page, wait):

        driver = start_from_login_page

        # нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.personal_account_button).click()
    
        # подождать загрузки кнопки "Выход" и нажать на неё
        wait.until(EC.visibility_of_element_located(Locators.exit_button))
        driver.find_element(*Locators.exit_button).click()

        # подождать перехода на страницу авторизации
        wait.until(EC.visibility_of_element_located(Locators.entrance_label))

        # ждём, что URL изменится на login_page
        wait.until(EC.url_to_be(login_page))

        # проверить, что мы на странице авторизации
        assert driver.current_url == login_page

  