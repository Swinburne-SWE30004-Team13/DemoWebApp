import unittest
from core.Operator import * 


class TestOperator(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2,4), 6, msg="Incorrect sum")
        self.assertEqual(sum(2,-4), -2, msg="Incorrect sum")
        self.assertEqual(sum(0, 0), 0, msg="Incorrect sum")


    def test_difference(self):
        self.assertEqual(difference(2,4), -2, msg="Incorrect sum")
        self.assertEqual(difference(2,-4), 6, msg="Incorrect sum")
        self.assertEqual(difference(0, 0), 0, msg="Incorrect sum")


    def test_product(self):
        self.assertEqual(product(2,4), 8, msg="Incorrect sum")
        self.assertEqual(product(2,-4), -8, msg="Incorrect sum")
        self.assertEqual(product(0, 0), 0, msg="Incorrect sum")

    def test_division(self):
        self.assertEqual(division(2,4), 0, msg="Incorrect sum")
        self.assertEqual(division(2,-4), -1, msg="Incorrect sum")
        self.assertEqual(division(0, 1), 0, msg="Incorrect sum")

if __name__ == '__main__':
    unittest.main()