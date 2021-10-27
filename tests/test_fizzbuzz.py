import unittest

from src.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_dummy(self):
        result = fizzbuzz()
        self.assertEqual(result, None)

    @unittest.SkipTest
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
