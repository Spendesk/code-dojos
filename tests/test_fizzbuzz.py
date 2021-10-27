import unittest

from src.fizzbuzz import fizzbuzz, loop_fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    # def test_dummy(self):
    #     result = fizzbuzz()
    #     self.assertEqual(result, None)


    def test_when_1_return_fizz(self):
        result = fizzbuzz(1)
        self.assertEqual(result, '1')

    def test_when_3_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, "fizz")

    def test_when_5_return_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual(result, "buzz")

    def test_when_15_return_buzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, "fizzbuzz")

    def test_when_9_return_fizz(self):
        result = fizzbuzz(9)
        self.assertEqual(result, "fizz")

    def test_when_10_return_buzz(self):
        result = fizzbuzz(10)
        self.assertEqual(result, "buzz")

    def test_when_30_return_buzz(self):
        result = fizzbuzz(30)
        self.assertEqual(result, "fizzbuzz")

    def test_loop_returns_5_times(self):
        expected_list = [
            '1',
            '2',
            'fizz',
            '4',
            'buzz'
        ]
        result = loop_fizzbuzz(5)
        self.assertEqual(result, expected_list)

    @unittest.SkipTest
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
