from praktikum.ingredient import Ingredient
import praktikum.ingredient_types
import allure

class TestIngredient:
    @allure.title("Создаем ингредиент и проверяем заданное название")
    def test_create_ingedient_and_return_name(self):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,'runch',5.5)
        assert ingredient.get_name() == 'runch'

    @allure.title("Создаем ингредиент и проверяем заданную цену")
    def test_create_ingedient_and_return_price(self):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,'bbq',7)
        assert ingredient.get_price() == 7
    
    @allure.title("Создаем ингредиент и проверяем заданный тип")
    def test_create_ingedient_and_return_type(self):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,'ketchup',2)
        assert ingredient.get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
