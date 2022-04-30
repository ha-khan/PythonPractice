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

        if not self.is_balanced(self.str):
            raise Exception('Not balanced!')
	
        # space ~ O(1)
        self.counter_0 = 0
        self.counter_1 = 0
        self.counter_2 = 0
    
    def is_balanced(self, s: str) -> bool:
        """
            is_balanced uses a stack abstract data type
            since we need to keep track of previously seen
            symbols/tokens, we can't use a regex as a DFA
            has no notion of "previous state" or "memory" 
            to make decisions off of, it uses what the current
            situation/state looks like and goes to the next state

            we need to make decisions on previous state so we need to 
            keep track of what that state was ... or what was seen previously

        """
        from queue import LifoQueue, Empty
        stack = LifoQueue()
        for rune in s:
            if rune in ['(', '[', '{']:
                stack.put(rune)
            else:
                try:
                    val = stack.get_nowait()
                    if val  != self.mapping[rune]:
                        return False
                except Empty:
                    return False
        return stack.empty() 
    
    def validate_0(self) -> bool:
        """
            solution works off of naive assumption that order of (){}[] doesn't matter
            only the count of it does, so )( would be considered a valid parenthesis
            which is probably incorrect

            need to keep track of when ) is seen, did we first have an equivalent ( ? 
        """
        for rune in self.str:
            self.counter.update([rune])
        
        return all([self.counter[x] == self.counter[y] for (x, y) in [('(',')'), ('{', '}'), ('[', ']')]]) 

    def validate_1(self) -> bool:
        for rune in self.str:
            if rune in ['(', '{', '[']:
                self.counter.update([rune])
                continue
            self.counter.subtract(self.mapping[rune])
        
        return all([self.counter[x] == 0 for (x, _) in [('(',')'), ('{', '}'), ('[', ']')]])

def main():
    v = ValidateParenthesis('({[]})()()()[]{}{}()')
    # print(f'Is valid: {v.validate_0()}')
    print(f'Is valid: {v.validate_1()}')
    try:
        v = ValidateParenthesis('{[(]}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
