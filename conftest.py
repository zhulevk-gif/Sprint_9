import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import BASE_URL, RECIPES_URL_PART, SIGNIN_URL_PART
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.registration_page import RegistrationPage
from page_objects.recipe_page import RecipePage
from test_data.user_data import unique_user


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.set_capability("acceptInsecureCerts", True)

    selenoid_uri = os.getenv("SELENOID_URI")
    if selenoid_uri:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", os.getenv("BROWSER_VERSION", "128.0"))
        options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": False})
        browser = webdriver.Remote(command_executor=selenoid_uri, options=options)
    else:
        browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver, base_url):
    return MainPage(driver, base_url)


@pytest.fixture
def registration_page(driver, base_url):
    return RegistrationPage(driver, base_url)


@pytest.fixture
def login_page(driver, base_url):
    return LoginPage(driver, base_url)


@pytest.fixture
def recipe_page(driver, base_url):
    return RecipePage(driver, base_url)


@pytest.fixture
def registered_user(main_page, registration_page, login_page):
    user = unique_user()

    main_page.open()
    main_page.open_registration_page()
    registration_page.register(user)

    login_page.current_url_contains(SIGNIN_URL_PART)
    login_page.is_login_form_visible()

    return user


@pytest.fixture
def authorized_user(main_page, login_page, registered_user):
    main_page.open()
    main_page.open_login_page()
    login_page.login(registered_user)

    main_page.current_url_contains(RECIPES_URL_PART)
    main_page.is_logout_button_visible()

    return registered_user