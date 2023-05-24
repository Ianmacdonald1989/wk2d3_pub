import unittest
from src.pub import *
from src.drinks import *
from src.customer import *
#Links the files together

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Joe", 10.00, 42, 0)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till_value(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    
    def test_check_age(self):
        result = self.pub.check_age(self.customer)
        self.assertEqual(True, result)