from praktikum.bun import Bun

class TestBun:
    def test_create_bun_and_return_bun_name(self):
        bun = Bun('black',10.5)
        assert bun.get_name() == 'black'

    def test_create_bun_and_return_bun_price(self):
        bun = Bun('black',10.5)
        assert bun.get_price() == 10.5
