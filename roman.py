import unittest

class RomanNumeralTest(unittest.TestCase):
    def test_result_of_one(self):
        self.assertEqual(roman_numerals(1), 'I')
    
    def test_result_of_two(self):
        self.assertEqual(roman_numerals(2), 'II')
    
    def test_result_of_three(self):
        self.assertEqual(roman_numerals(3), 'III')

    def test_result_of_four(self):
        self.assertEqual(roman_numerals(4), 'IV')
    
    def test_result_of_five(self):
         self.assertEqual(roman_numerals(5), 'V')
    
    def test_result_of_six(self):
         self.assertEqual(roman_numerals(6), 'VI')

    def test_result_of_eight(self):
         self.assertEqual(roman_numerals(8), 'VIII')
    
    def test_result_of_nine(self):
         self.assertEqual(roman_numerals(9), 'IX')

    def test_result_of_ten(self):
        self.assertEqual(roman_numerals(10), 'X')
    
    def test_result_of_eleven(self):
        self.assertEqual(roman_numerals(11), 'XI')

    def test_result_of_fourteen(self):   
        self.assertEqual(roman_numerals(14), 'XIV')


def roman_numerals(number):
    roman_string = []
    four = 'IV'
    five = 'X'
    nine = 'IX'

    if number >= 10 and number < 40:
        number = int(number / 3)
        print(number)
        for i in range(number):
            roman_string.append('X')
        print(roman_string)
    if number < 4:
        for i in range(number):
            roman_string.append('I')
    
    if str(number).endswith('4'):
        roman_string.append(four)
        
    # elif number == 4:
    #     roman_string.append('IV')
    # elif number == 5:
    #     roman_string.append('V')
    # elif number > 5 and number < 9:
    #     roman_string.append('V')
    #     for i in range(number - 5):
    #         roman_string.append('I')
    # elif number == 9:
    #     roman_string.append('IX')
    # elif number == 10:
    #     roman_string.append('X')
    # elif number > 10 and number < 14:
    #     roman_string.append('X')
    #     for i in range(number - 10):
    #         roman_string.append('I')
    # elif number == 14:
    #     roman_string.append('XIV')       

    return ''.join(roman_string)

if __name__ == '__main__':
    unittest.main()