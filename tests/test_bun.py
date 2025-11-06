from praktikum.bun import Bun
import allure

class TestBun:
    @allure.title("Создаем булочку для бургера и проверяем заданное имя")
    def test_create_bun_and_return_bun_name(self):
        bun = Bun('black',10.5)
        assert bun.get_name() == 'black'

    @allure.title("Создаем булочку для бургера и проверяем заданную цену")
    def test_create_bun_and_return_bun_price(self):
        bun = Bun('black',10.5)
        assert bun.get_price() == 10.5
