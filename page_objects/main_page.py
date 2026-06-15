import allure

from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Перейти на страницу регистрации")
    def open_registration_page(self):
        self._click(MainPageLocators.CREATE_ACCOUNT_LINK)

    @allure.step("Перейти на страницу авторизации")
    def open_login_page(self):
        self._click(MainPageLocators.LOGIN_LINK)

    @allure.step("Перейти на страницу создания рецепта")
    def open_recipe_creation_page(self):
        self._click(MainPageLocators.CREATE_RECIPE_LINK)

    @allure.step("Проверить, что кнопка 'Выход' отображается")
    def is_logout_button_visible(self) -> bool:
        return self._is_visible(MainPageLocators.LOGOUT_LINK)