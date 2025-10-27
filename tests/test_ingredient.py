from praktikum.ingredient import Ingredient
import praktikum.ingredient_types

class TestIngredient:
    def test_create_ingedient_and_return_name(self):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,'runch',5.5)
        assert ingredient.get_name() == 'runch'

    def test_create_ingedient_and_return_price(self):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,'bbq',7)
        assert ingredient.get_price() == 7

    def test_create_ingedient_and_return_type(self):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE,'ketchup',2)
        assert ingredient.get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
