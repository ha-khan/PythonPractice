"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
1


"""
from collections import Counter

class ValidateParenthesis:
    def __init__(self, s: str) -> None:
        self.str = s

        # space ~ O(n)
        self.counter = Counter()
        self.mapping = {')':'(', '}':'{', ']':'['}
	
        # space ~ O(1)
        self.counter_0 = 0
        self.counter_1 = 0
        self.counter_2 = 0

    def validate_0(self) -> bool:
        for rune in self.str:
            if rune in ['(', '{', '[']:
                self.counter.update([rune])
                continue
            self.counter.subtract(self.mapping[rune])
                 
        return all([self.counter[x] == self.counter[y] for (x, y) in [('(',')'), ('{', '}'), ('[', ']')]])

def main():
    v = ValidateParenthesis('(]')
    print(f'Is valid: {v.validate_0()}')


if __name__ == '__main__':
    main()

