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

    # def test_result_of_eight(self):
    #      self.assertEqual(roman_numerals(8), 'VIII')
    
    # def test_result_of_nine(self):
    #      self.assertEqual(roman_numerals(9), 'IX')

    # def test_result_of_ten(self):
    #     self.assertEqual(roman_numerals(10), 'X')
    
    # def test_result_of_eleven(self):
    #     self.assertEqual(roman_numerals(11), 'XI')

    # def test_result_of_fourteen(self):   
        # self.assertEqual(roman_numerals(14), 'XIV')


def roman_numerals(number):
    roman_string = []
    remainder = number % 5
    roman_to_num_dict = {
        1: 'I', 4: 'IV', 5: 'V', 10:'X', 50:'L'
    }

    if number < 4:
        return roman_to_num_dict[1] * number

    if number in roman_to_num_dict:
        roman_string.append(roman_to_num_dict[number])
    elif (number - remainder) in roman_to_num_dict:
        roman_string.append(roman_to_num_dict[number - remainder])
        roman_string.append(roman_to_num_dict[remainder])
        print(roman_string)

    return "".join(roman_string)
        
    
    

if __name__ == '__main__':
    unittest.main()