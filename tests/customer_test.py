import unittest
from src.customer import *
from src.drinks import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Joe", 10.00, 42, 0)


    def test_reduce_wallet(self):
        self.customer.reduce_wallet(2.50)
        self.assertEqual(7.50, self.customer.wallet)


    def test_increase_alcohol_level(self):
        alcohol_level = 3
        result = self.customer.increase_alcohol_level(alcohol_level)
        self.assertEqual(result, 3) 
    
    def test_refuse(self):
       drunkenness_level = 12
       result = self.customer.refuse(drunkenness_level)
       self.assertEqual("LEAVE", result)