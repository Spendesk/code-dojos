import unittest

from src.fizzbuzz import sum


class TestFizzBuzz(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [1/4, 1/4, 2/5]
        result = sum(data)
        self.assertEqual(result, 0.9)

    @unittest.SkipTest
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
