from praktikum.burger import Burger
from unittest.mock import Mock
import praktikum.ingredient_types
import allure

class TestBurger:
    @allure.title("Задаем булочку для бургера и проверяем установленное название булочки")
    def test_burger_set_buns_and_return_name(self):
        mock_bun = Mock()
        mock_bun.name = 'black'
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == 'black'

    @allure.title("Задаем ингредиент для бургера и проверяем установленное значение")
    def test_burger_add_ingredient_and_return_list(self):
        mock_ingredient = Mock()
        mock_ingredient.type = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = 'runch'
        mock_ingredient.price = 5.5
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient
    
    @allure.title("Проверяем удаление ингредиента из списка")
    def test_burger_remove_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = 'runch'
        mock_ingredient.price = 5.5
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []
    
    @allure.title("Проверяем изменение ингредиентов в списке")
    def test_burger_move_ingredient(self):
        mock_ingredient0 = Mock()
        mock_ingredient0.type = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient0.name = 'runch'
        mock_ingredient0.price = 5.5
        mock_ingredient1 = Mock()
        mock_ingredient1.type = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient1.name = 'bbq'
        mock_ingredient1.price = 7.5
        burger = Burger()
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] ==  mock_ingredient1
    
    @allure.title("Проверяем расчет цены для булочки бургера")
    def test_burger_get_price_of_bun(self):     
        mock_bun = Mock()
        mock_bun.get_price.return_value = 5.0
        burger = Burger() 
        burger.set_buns(mock_bun)
        assert burger.get_price() == 10.0

    @allure.title("Проверяем расчет цены всего бургера с булочкой и ингредиентами")
    def test_burger_get_price_of_full_burger(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 5.0
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 5.5
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 15.5
    
    @allure.title("Проверяем получение чека и цены всего бургера")
    def test_burger_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'black'
        mock_bun.get_price.return_value = 5.0
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = 'runch'
        mock_ingredient.get_price.return_value = 5.5
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)       
        assert burger.get_receipt() == '(==== black ====)\n= sauce runch =\n(==== black ====)\n\nPrice: 15.5'
