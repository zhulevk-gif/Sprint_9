from selenium.webdriver.common.by import By


class RecipeLocators:
    NAME_INPUT = (By.XPATH, "//div[normalize-space()='Название рецепта']/ancestor::label//input")
    INGREDIENT_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsInput')]")
    INGREDIENT_OPTION = (By.XPATH, "//div[normalize-space()='{ingredient}']")
    AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//*[self::button or self::div][normalize-space()='Добавить ингредиент']")
    ADDED_INGREDIENT = (By.XPATH, "//*[contains(normalize-space(), '{ingredient}') and contains(normalize-space(), '{amount}')]")
    COOKING_TIME_INPUT = (By.XPATH, "//div[normalize-space()='Время приготовления']/ancestor::label//input")
    TEXTAREA = (By.TAG_NAME, "textarea")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать рецепт']")
    RECIPE_CARD_BY_NAME = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'recipe')][.//*[normalize-space()='{name}'] or contains(., '{name}')]")
    TITLE_BY_NAME = (By.XPATH, "//*[contains(normalize-space(), '{name}')]")
