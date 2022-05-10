# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# 
# Return the answer in any order.
#
#  A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#  
#
#  [1 ->     ] [2 -> abc ] [3 -> def ]
#  [4 -> ghi ] [5 -> jkl ] [6 -> mno ]
#  [7 -> pqrs] [8 -> tuv ] [9 -> wxyz]
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
#
# Input: digits = ""
# Output: []
#
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
# Constraints:
#
#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9']
from typing import List

class EnumeratePhoneNumber:
    def __init__(self, digits: str) -> None:
        self.digits = digits
        self.button_map = {
            '1' : '',
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
    
    def __call__(self) -> List[str]:
        strs = []

        def recurse(remainder_str: str, current_str: str):
            # base case
            if remainder_str == '':
                strs.append(current_str)
                return
            
            head = remainder_str[0]
            tail = remainder_str[1:]
            for rune in self.button_map[head]:
                recurse(tail, current_str+rune)
        
        if self.digits != '': recurse(self.digits, "")
        
        return strs

def main():
    print(EnumeratePhoneNumber("23")())
    print(EnumeratePhoneNumber("")())
    print(EnumeratePhoneNumber("2")())

if __name__ == '__main__':
    main()
