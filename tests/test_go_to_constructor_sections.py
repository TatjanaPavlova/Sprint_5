import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestGoToConstructorSections:

    @pytest.mark.parametrize("tab_locator, active_tab_locator, temp_tab_locator", [
    (Locators.buns_tab, Locators.active_buns_tab, Locators.sauces_tab),  # вкладка "Булки" (сначала кликаем на "Соусы", чтобы проверить переход)
    (Locators.sauces_tab, Locators.active_sauces_tab, None), # вкладка "Соусы"
    (Locators.fillings_tab, Locators.active_fillings_tab, None), # вкладка "Начинки"
])
    def test_navigation_to_constructor_sections(self, start_from_login_page, tab_locator, active_tab_locator, temp_tab_locator):

        driver = start_from_login_page
        wait = WebDriverWait(driver, 10)

        # Если есть временная вкладка (для раздела "Булки"), сначала кликнуть по ней
        if temp_tab_locator:
            temp_element = wait.until(EC.element_to_be_clickable(temp_tab_locator))
            temp_element.click()

        # кликнуть по вкладке
        tab_element = wait.until(EC.element_to_be_clickable(tab_locator))
        tab_element.click()

        # проверяем, что вкладка стала активной
        assert wait.until(EC.visibility_of_element_located(active_tab_locator))