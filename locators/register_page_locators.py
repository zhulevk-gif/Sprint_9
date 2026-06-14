from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    USERNAME_INPUT = (By.NAME, "username")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form button[type='submit']")