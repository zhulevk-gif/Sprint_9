import allure

from locators.login_locators import LoginLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Авторизоваться пользователем")
    def login(self, user):
        self._type(LoginLocators.EMAIL_INPUT, user.username)
        self._type(LoginLocators.PASSWORD_INPUT, user.password)
        self._click(LoginLocators.SUBMIT_BUTTON)

    @allure.step("Проверить, что форма авторизации отображается")
    def is_login_form_visible(self) -> bool:
        return self._is_visible(LoginLocators.FORM)