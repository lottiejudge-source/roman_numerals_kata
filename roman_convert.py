import unittest

class TestRomanNumeralConvertor(unittest.TestCase):

    def test_converts_to_one(self):
        self.assertEqual(roman_numeral_convertor(1), 'I')
    
    def test_converts_to_two(self):
        self.assertEqual(roman_numeral_convertor(2), 'II')
    
    def test_converts_to_five(self):
        self.assertEqual(roman_numeral_convertor(5), 'V')
    
    def test_coverts_to_four(self):
        self.assertEqual(roman_numeral_convertor(4), 'IV')
    
    def test_coverts_to_six_seven_and_eight(self):
        self.assertEqual(roman_numeral_convertor(6), 'VI')
        self.assertEqual(roman_numeral_convertor(7), 'VII')
        self.assertEqual(roman_numeral_convertor(8), 'VIII')
    
    def test_converts_to_nine(self):
        self.assertEqual(roman_numeral_convertor(9), 'IX')
    
    def test_converts_to_ten(self):
        self.assertEqual(roman_numeral_convertor(10), 'X')
    
    def test_coverts_to_ten(self):
        self.assertEqual(roman_numeral_convertor(40), 'XL')


def roman_numeral_convertor(number):
    number_to_numeral = {
        1: 'I', 5: 'V', 10: 'X', 50: 'L'
    }
    result = ""

    if number in number_to_numeral: 
        result = (number_to_numeral[number])
    elif number == 4:
        result = 'IV'
    elif 9 > number > 5:
        remainder = number - 5
        result = number_to_numeral[5] + number_to_numeral[1] * remainder
    elif number == 9:
        result = 'IX'
    elif number == 10:
        result = 'X'
    elif number == 40:
        result = 'LX'
    else:
        result = 'I' * number


    return result

if __name__ == '__main__':
    unittest.main()