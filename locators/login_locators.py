from selenium.webdriver.common.by import By


class LoginLocators:
    FORM = (By.XPATH, "//form[.//input[@name='email'] and .//input[@name='password']]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
