import unittest
from Homework27 import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(17))

if __name__ == '__main__':
    unittest.main()