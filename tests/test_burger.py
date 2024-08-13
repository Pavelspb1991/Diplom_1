from burger import Burger
from conftest import mock_bun, mock_sauce, mock_filling
import pytest
from data_for_test import DataForTest


class TestBurger:

    def test_set_bonus_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize("data", [DataForTest.sauce, DataForTest.filling])
    def test_add_ingredient_success(self, data, mock_sauce, mock_filling):
        burger = Burger()
        if data['ingredient'] == 'mock_sauce':
            burger.add_ingredient(mock_sauce)
        elif data['ingredient'] == 'mock_filling':
            burger.add_ingredient(mock_filling)
        else:
            raise ValueError("Неверный тип ингредиента")
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == data['expected_name']
        assert burger.ingredients[0].get_price() == data['expected_price']
        assert burger.ingredients[0].get_type() == data['expected_type']

    def test_remove_ingredient_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        ingredient_names = [ingredient.get_name() for ingredient in burger.ingredients]
        assert mock_filling.get_name() not in ingredient_names

    def test_move_ingredient_success(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_filling

    def test_get_price_success(self, mock_bun, mock_filling, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == DataForTest.total_burger_price

    def test_get_receipt_success(self, mock_bun, mock_filling, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        assert burger.get_receipt() == DataForTest.receipt
