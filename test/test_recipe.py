import allure

from test_data.user_data import unique_recipe


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.title("Авторизованный пользователь может создать рецепт")
    def test_authorized_user_can_create_recipe(self, base_page, recipe_page, authorized_user):
        recipe = unique_recipe()

        base_page.open()
        base_page.click_create_recipe()
        recipe_page.create_recipe(recipe)

        assert recipe_page.is_recipe_card_visible(recipe.name)
        assert recipe_page.is_recipe_title_visible(recipe.name)
