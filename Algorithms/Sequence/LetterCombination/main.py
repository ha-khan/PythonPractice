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
        """
            Problem calls for all possible combinations, which is usually
            an enumeration that can be done with recursion where a base case 
            would stop the enumeration, meaning we've reached the end

            in this we are recursing over the inputted digits string where
            we grab the head at each recursive call and from that we iterate over each 
            entry in the button_map and build a possible string entry

            when recursive calls reach the base case, we can't recurse further from an 
            empty string, so we record the built string thus far into 

            time  ~ O(3^n), where n is the length of the inputted digits
            space ~ O(3^n), where n is the length of the inputted digits

            there are generally 3 recursive calls generated for each entry of a digit

            so, if a digit has entry 1, 2

            3 * 3
        """
        solution = []

        def recurse(remainder_str: str, current_str: str):
            # base case
            if remainder_str == '':
                solution.append(current_str)
                return
            
            head = remainder_str[0]
            tail = remainder_str[1:]
            for rune in self.button_map[head]:
                recurse(tail, current_str+rune)
        
        if self.digits != '': recurse(self.digits, "")
        
        return solution
    
    def enumerate_with_iteration(self) -> List[str]:
        """
        
        """
        solution = ['']
        for rune in self.digits:
            buffer = []
            for numeral in self.button_map[rune]:
                for runes in solution:
                    buffer.append(runes+numeral)
            solution = list(buffer)

        return solution 

def main():
    print(EnumeratePhoneNumber('23')())
    print(EnumeratePhoneNumber('')())
    print(EnumeratePhoneNumber('2')())
    print(EnumeratePhoneNumber('23').enumerate_with_iteration())
    assert sorted(EnumeratePhoneNumber('456')()) == sorted(EnumeratePhoneNumber('456').enumerate_with_iteration())

if __name__ == '__main__':
    main()
