from data_for_test import DataForTest
from bun import Bun


class TestBun:

    def test_get_name_bun_success(self):
        bun = Bun(DataForTest.bun['expected_name'], DataForTest.bun['expected_price'])
        assert bun.get_name() == DataForTest.bun['expected_name']

    def test_get_price_bun_success(self):
        bun = Bun(DataForTest.bun['expected_name'], DataForTest.bun['expected_price'])
        assert bun.get_price() == DataForTest.bun['expected_price']