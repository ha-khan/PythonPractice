"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8
"""
from queue import Empty
from typing import List

class GenerateParenthesis:
    def __init__(self, n: int) -> None:
        self.n = n*2
    
    def __call__(self) -> List[str]:
        return self.solution_0()

    @staticmethod 
    def is_balanced(s: str) -> bool:
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
        from queue import LifoQueue 
        stack = LifoQueue()
        for rune in s:
            if rune in ['(']:
                stack.put('(')
            else:
                try:
                    stack.get_nowait()
                except Empty:
                    return False
        return stack.empty() 

    def solution_0(self) -> List[str]:
        """
            enumerate all possible strings with given amount of (, )
            and check to ensure that every (, ) is evenly balanced

            time ~ O(2^n)
            space ~ O(2n) if ignoring recursive callstack
        """
        buffer = []
        def enumerate_(s: str)-> None:
            for rune in ['(', ')']:
                if len(s) == self.n:
                    buffer.append(s)
                    return
                enumerate_(s+rune)
        enumerate_('')
        return [s for s in filter(self.is_balanced, buffer)]
    
def main():
    s = GenerateParenthesis(3)
    print(f'Input: n = {int(s.n/2)}\nOutput: {s()}')
    print(s.is_balanced('(())()'))
    print(s.solution_0())

if __name__ == '__main__':
    main()
    