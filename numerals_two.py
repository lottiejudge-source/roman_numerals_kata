import unittest

class TestRomanNumerals(unittest.TestCase):

    def test_converts_1_to_I(self):
        self.assertEqual(convert_to_numerals(1), 'I')

    def test_converts_2_to_II(self):
        self.assertEqual(convert_to_numerals(2), 'II')

    def test_converts_3_to_III(self):
        self.assertEqual(convert_to_numerals(3), 'III')

    def test_converts_4_to_IV(self):
        self.assertEqual(convert_to_numerals(4), 'IV')
    
    def test_converts_5_to_V(self):
        self.assertEqual(convert_to_numerals(5), 'V')

    def test_converts_6_to_VI(self):
        self.assertEqual(convert_to_numerals(6), 'VI')

    def test_converts_numbers_between_6_and_8(self):
        self.assertEqual(convert_to_numerals(6), 'VI')
        self.assertEqual(convert_to_numerals(7), 'VII')
        self.assertEqual(convert_to_numerals(8), 'VIII')

def convert_to_numerals(number):
    numeral = {
        1: 'I',
        5: 'V'
    }

    if number == 4:
        return numeral[1]+numeral[5]
    if number == 5:
        return numeral[5]
    if 5 < number < 9:
        remainder = number - 5
        return numeral[5] + (numeral[1] * remainder)
    return 'I' * number

if __name__ == '__main__':
    unittest.main()

# numeral = {
#         1: 'I',
#         5: 'V',
#         10: 'X',
#         50: 'L',
#         100: 'C',
#         500: 'D',
#         1000: 'M'
#         }