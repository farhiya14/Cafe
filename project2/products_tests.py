from io import StringIO
from unittest.mock import patch

from products import products_listed

def test_add_item_adds_item_to_collection():
    available_products = [
        {'id': 1, 'name': 'Coke', 'price': 0.8},
        {'id': 2, 'name': 'Smart Water', 'price': 0.95},
        {'id': 3, 'name': 'Pepsi Max', 'price': 0.7},
        {'id': 5, 'name': 'Fanta', 'price': 0.65},
    ]

    product_to_add = {"id": 6, "name": "Mountain Dew", "price": 1.15}

    expected = [
        {'id': 1, 'name': 'Coke', 'price': 0.8},
        {'id': 2, 'name': 'Smart Water', 'price': 0.95},
        {'id': 3, 'name': 'Pepsi Max', 'price': 0.7},
        {'id': 5, 'name': 'Fanta', 'price': 0.65},
        {"id": 6, "name": "Mountain Dew", "price": 1.15},
    ]

    actual = products_listed.add_item(product_to_add, available_products)

    assert expected == actual

test_add_item_adds_item_to_collection()

