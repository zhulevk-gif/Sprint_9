import allure

from locators.registration_locators import RegistrationLocators
from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    @allure.step("Зарегистрировать нового пользователя")
    def register(self, user):
        self._type(RegistrationLocators.FIRST_NAME_INPUT, user.first_name)
        self._type(RegistrationLocators.LAST_NAME_INPUT, user.last_name)
        self._type(RegistrationLocators.USERNAME_INPUT, user.username)
        self._type(RegistrationLocators.EMAIL_INPUT, user.email)
        self._type(RegistrationLocators.PASSWORD_INPUT, user.password)
        self._click(RegistrationLocators.SUBMIT_BUTTON)