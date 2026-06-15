from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[normalize-space()='Создать аккаунт']")
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")
    LOGOUT_LINK = (By.XPATH, "//*[self::a or self::button][normalize-space()='Выход']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[normalize-space()='Создать рецепт']")