import allure

from test_data.user_data import unique_user


@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("После регистрации пользователь попадает на страницу авторизации")
    def test_registration_redirects_to_login_page(self, base_page, registration_page, login_page):
        user = unique_user()

        base_page.open()
        base_page.click_create_account()
        registration_page.register(user)

        assert login_page.current_url_contains("signin")
        assert login_page.is_login_form_visible()
