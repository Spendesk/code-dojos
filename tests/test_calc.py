import unittest

from src.calc import add


class TestSum(unittest.TestCase):

    def test_return_0_if_empty(self):
        # Given
        input = ""

        # When
        output = add(input)

        # Then
        self.assertEqual(output,"0")

    def test_when_12_then_3(self):
        # Given
        input = "1,2"

        # When
        output = add(input)

        # Then
        self.assertEqual(output,"3")

    def test_when_1222_then_33(self):
    # Given
        input = "1.1,2.2"

        # When
        output = add(input)

        # Then
        self.assertEqual(output,"3.3")

    def test_when_missing_number_then_error(self):
    # Given
        input = "175.2,\n35"

        # When
        output = add(input)

        # Then
        self.assertEqual(output,"Number expected but '\n' found at position 6.")

    def test_when_1_2_3_with_new_line_then_6(self):
    # Given
        input = "1\n2,3"

        # When
        output = add(input)

        # Then
        self.assertEqual(output,"6")


if __name__ == '__main__':
    unittest.main()
