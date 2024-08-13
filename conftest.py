import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Краторная булочка'
    mock_bun.get_price.return_value = 1255
    return mock_bun


@pytest.fixture
def mock_sauce():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = 'Соус Spicy'
    mock_for_sauce.get_price.return_value = 90
    mock_for_sauce.get_type.return_value = 'SAUCE'
    return mock_for_sauce


@pytest.fixture
def mock_filling():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = 'Говяжий метеорит (отбивная)'
    mock_for_filling.get_price.return_value = 3000
    mock_for_filling.get_type.return_value = 'FILLING'
    return mock_for_filling
