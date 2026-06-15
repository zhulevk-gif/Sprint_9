import allure

from constants import SIGNIN_URL_PART
from test_data.user_data import unique_user


@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("После регистрации пользователь попадает на страницу авторизации")
    def test_registration_redirects_to_login_page(self, main_page, registration_page, login_page):
        user = unique_user()

        main_page.open()
        main_page.open_registration_page()
        registration_page.register(user)

        assert login_page.current_url_contains(SIGNIN_URL_PART)
        assert login_page.is_login_form_visible()