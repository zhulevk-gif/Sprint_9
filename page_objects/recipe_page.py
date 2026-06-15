from pathlib import Path

import allure

from locators.recipe_locators import RecipeLocators
from page_objects.base_page import BasePage


PROJECT_DIR = Path(__file__).resolve().parents[1]


class RecipePage(BasePage):
    @allure.step("Создать рецепт")
    def create_recipe(self, recipe):
        self._type(RecipeLocators.NAME_INPUT, recipe.name)
        self._add_ingredient(recipe.ingredient_search, recipe.ingredient, recipe.amount)
        self._type(RecipeLocators.COOKING_TIME_INPUT, recipe.cooking_time)
        self._type(RecipeLocators.TEXTAREA, recipe.text)
        self._find_present(RecipeLocators.FILE_INPUT).send_keys(
            str(self._recipe_image_path(recipe.image_name))
        )
        self._click(RecipeLocators.SUBMIT_BUTTON)

    @allure.step("Проверить, что карточка рецепта '{recipe_name}' отображается")
    def is_recipe_card_visible(self, recipe_name: str) -> bool:
        return self._is_visible(
            self._format_locator(RecipeLocators.RECIPE_CARD_BY_NAME, name=recipe_name)
        )

    @allure.step("Проверить, что название рецепта '{recipe_name}' отображается")
    def is_recipe_title_visible(self, recipe_name: str) -> bool:
        return self._is_visible(
            self._format_locator(RecipeLocators.TITLE_BY_NAME, name=recipe_name)
        )

    @staticmethod
    def _recipe_image_path(image_name: str) -> Path:
        return PROJECT_DIR / "assets" / image_name

    @allure.step("Добавить ингредиент '{ingredient}' в количестве '{amount}'")
    def _add_ingredient(self, search_text: str, ingredient: str, amount: str):
        self._type(RecipeLocators.INGREDIENT_INPUT, search_text)
        self._click_text(ingredient)
        self._type(RecipeLocators.AMOUNT_INPUT, amount)
        self._click_text("Добавить ингредиент")
        self._is_visible(
            self._format_locator(
                RecipeLocators.ADDED_INGREDIENT,
                ingredient=ingredient,
                amount=amount,
            )
        )

    @staticmethod
    def _format_locator(locator, **kwargs):
        by, value = locator
        return by, value.format(**kwargs)