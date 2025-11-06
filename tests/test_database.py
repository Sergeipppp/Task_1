from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest
import allure

class TestDatabase:
    @allure.title("Проверяем инициализацию базы данных")
    def test_init_database(self):
        db = Database()
        assert len(db.buns) == 3 and len(db.ingredients) == 6
    
    @allure.title("Проверяем доступные булочки в базе данных")
    @pytest.mark.parametrize(
    'index,name,price',
    [
        [0,'black bun', 100],
        [1,'white bun', 200],
        [2,'red bun', 300]
    ])
    def test_database_available_buns(self, index, name, price):
        db = Database()
        assert db.available_buns()[index].name == name and db.available_buns()[index].price == price

    @allure.title("Проверяем доступные ингредиенты в базе данных")
    @pytest.mark.parametrize(
    'index,type,name,price',
    [
        [0,INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [1,INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [2,INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [3,INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [4,INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [5,INGREDIENT_TYPE_FILLING, "sausage", 300]
    ])
    def test_database_available_ingredients(self, index, type, name, price):
        db = Database()
        assert db.available_ingredients()[index].type == type and db.available_ingredients()[index].name == name and db.available_ingredients()[index].price == price
