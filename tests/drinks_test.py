import unittest
from src.drinks import *
from src.customer import *

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = [
            {
                "name": "Beer",
                "price": 2.50,
                "alcohol_level": 3
            },
            {
                "name": "Wine",
                "price": 3,
                "alcohol_level": 3
            },
            {
                "name": "Cider",
                "price": 3.50,
                "alcohol_level": 3
            }
        ]    