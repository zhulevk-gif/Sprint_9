import allure


@allure.feature("Авторизация")
class TestLogin:
    @allure.title("Зарегистрированный пользователь может авторизоваться")
    def test_registered_user_can_login(self, base_page, login_page, registered_user):
        base_page.open()
        base_page.click_login()
        login_page.login(registered_user)

        assert base_page.current_url_contains("recipes")
        assert base_page.is_logout_button_visible()
