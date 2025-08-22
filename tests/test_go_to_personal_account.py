from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestGoToPersonalAccountFromMainPage:

    def test_redirect_to_personal_account(self, start_from_login_page, wait):

        driver = start_from_login_page

        # нажать на кнопку "Личный кабинет"
        driver.find_element(*Locators.personal_account_button).click()

        # подождать загрузки кнопки "Профиль"
        wait.until(EC.visibility_of_element_located(Locators.profile_button))

        # ждём, что URL изменится на main_page
        wait.until(EC.url_to_be(profile_page))

        # проверить, что мы в личном кабинете
        assert driver.current_url == profile_page