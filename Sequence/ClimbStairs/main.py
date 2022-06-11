# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# 
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# 
#
# Constraints:
#     1 <= n <= 45
from typing import Any
from pprint import pprint


class ClimbStairs:
    def __init__(self, n: int) -> None:
        self.n = n
        self.buffer = []
    
    def __call__(self, *args: Any, **kwargs: Any) -> int:
        """
        """
        try:
            fn = getattr(self, args[0])
            return fn()
        except (AttributeError, IndexError):
            return -1

    def _solution_0(self):
        """
            top-down recursion 
        """
        from functools import cache

        @cache
        def recurse(n: int) -> int:
            if n == 0:
                return 1 
            if n < 0:
                return 0
            return recurse(n - 1) + recurse(n - 2)
        return recurse(self.n)
    
    def _solution_1(self) -> int:
        """
            bottom-up recursion
        """
        from functools import cache

        @cache
        def recurse(n: int) -> int:
            if n == self.n:
                return 1
            if n > self.n:
                return 0
            return recurse(n + 1) + recurse(n + 2)
        return recurse(0)  
    
    def _solution_2(self) -> int:
        """
            using the built-in map container 
        """
        cache = dict()

        def recurse(n: int) -> int:
            if n == 0:
                return 1
            if n < 0:
                return 0
            a = 0 
            if n - 1 in cache:
                a = cache[n-1]
            else: 
                cache[n-1] = recurse(n-1)
                a = cache[n -1]
            b = 0
            if n - 2 in cache:
                b = cache[n - 2]
            else:
                cache[n-2] = recurse(n - 2)
                b = cache[n-2]
            return a + b
        return recurse(self.n)

    def _solution_3(self) -> int:
        """
        Can solve by enumerating through all solutions of 
        
        1*x + 2*y = n

        and counting all unique permutations 

        time  ~ O()
        space ~ O()

        """
        from math import ceil
        solutions = list()
        
        for x in range(self.n + 1):
            for y in range(ceil(self.n / 2) + 1):
                if (1*x+ 2*y) == self.n:
                    ones = '1 + '*x
                    twos = '2 + '*y
                    buffer = f'{ones[:len(ones) - 3]} + {twos[:len(twos) - 3]}'
                    solutions.append(buffer)
        print(solutions)
        return len(solutions)
        

def main():
    c = ClimbStairs(23)
    pprint(c._solution_0())

    c = ClimbStairs(23)
    pprint(c._solution_1())

    c = ClimbStairs(23)
    pprint(c._solution_2())


if __name__ == '__main__':
    main()
