import pytest
from ingredient import Ingredient
from data_for_test import DataForTest


class TestIngredient:

    @pytest.mark.parametrize("data", [DataForTest.sauce, DataForTest.filling])
    def test_get_name_success(self, data):
        ingredient = Ingredient(data['expected_type'], data['expected_name'], data['expected_price'])
        assert ingredient.get_name() == data['expected_name']

    @pytest.mark.parametrize("data", [DataForTest.sauce, DataForTest.filling])
    def test_get_price_success(self, data):
        ingredient = Ingredient(data['expected_type'], data['expected_name'], data['expected_price'])
        assert ingredient.get_price() == data['expected_price']

    @pytest.mark.parametrize("data", [DataForTest.sauce, DataForTest.filling])
    def test_get_type_success(self, data):
        ingredient = Ingredient(data['expected_type'], data['expected_name'], data['expected_price'])
        assert ingredient.get_type() == data['expected_type']