class DataForTest:
    sauce = {
        'ingredient': 'mock_sauce',
        'expected_name': 'Соус Spicy',
        'expected_price': 90,
        'expected_type': 'SAUCE'
    }
    filling = {
        'ingredient': 'mock_filling',
        'expected_name': 'Говяжий метеорит (отбивная)',
        'expected_price': 3000,
        'expected_type': 'FILLING'
    }

    bun = {
        'ingredient': 'mock_bun',
        'expected_name': 'Краторная булочка',
        'expected_price': 1255,
        'expected_type': 'BUN'
    }

    total_burger_price = sauce['expected_price'] + filling['expected_price'] + bun['expected_price'] * 2

    receipt = ('(==== Краторная булочка ====)\n'
                                        '= filling Говяжий метеорит (отбивная) =\n'
                                        '= sauce Соус Spicy =\n'
                                        '(==== Краторная булочка ====)\n'
                                        '\n'
                                        'Price: 5600')
