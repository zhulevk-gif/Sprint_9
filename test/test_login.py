import allure

from constants import RECIPES_URL_PART


@allure.feature("Авторизация")
class TestLogin:
    @allure.title("Зарегистрированный пользователь может авторизоваться")
    def test_registered_user_can_login(self, main_page, login_page, registered_user):
        main_page.open()
        main_page.open_login_page()
        login_page.login(registered_user)

        assert main_page.current_url_contains(RECIPES_URL_PART)
        assert main_page.is_logout_button_visible()