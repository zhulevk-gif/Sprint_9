import allure

from data.credentials import generate_user_data
from data.urls import LOGIN_URL, REGISTER_URL
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


@allure.feature("Авторизация")
class TestAuth:

    @allure.title("Пользователь может авторизоваться")
    def test_user_can_login(self, driver):
        register_page = RegisterPage(driver)
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)

        user_data = generate_user_data()

        register_page.open(REGISTER_URL)
        register_page.register(user_data)

        auth_page.wait_for_url_contains("signin")
        auth_page.open(LOGIN_URL)
        auth_page.login(user_data["username"], user_data["password"])

        assert main_page.is_current_url_contains("/")