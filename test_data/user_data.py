from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


@dataclass(frozen=True)
class Recipe:
    name: str
    ingredient: str
    ingredient_search: str
    amount: str
    cooking_time: str
    text: str
    image_name: str = "recipe.bmp"


def unique_user() -> User:
    suffix = uuid4().hex[:8]
    return User(
        first_name="Автотест",
        last_name=f"Пользователь {suffix}",
        username=f"autotest_{suffix}",
        email=f"autotest_{suffix}@example.com",
        password="StrongPassword123",
    )


def unique_recipe() -> Recipe:
    suffix = uuid4().hex[:8]
    return Recipe(
        name=f"Автотест рецепт {suffix}",
        ingredient="маасдам",
        ingredient_search="м",
        amount="1",
        cooking_time="5",
        text="Рецепт создан автотестом Selenium.",
    )
