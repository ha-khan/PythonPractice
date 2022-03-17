from re import I


class LongestPalindromicSubstring:
    """
        Longest Palindromic Substring is a Class that creates instances objects 
        that can compute what the longest palindroming substring in a given str is.
    """
    import math

    def __init__(self, input: str) -> None:
        self.input = input

    def compute_iteration(self) -> int:
        """
            Iteratively enumerate all possible substrings within a given range, check each one whether or not palindrome
            if yes, then compute length and keep track of longest seen plaindrome seen thus far

            we need to enumerate all possible substrings exactly once so quadratic time is not avoidable 
            time  ~ O(n^2)
            space ~ O(1) 

        """
        longest = 0
        for idx, _ in enumerate(self.input):
            for idy in range(idx, len(self.input)+1):
                if idx == idy: continue
                if self.is_palindromic(self.input[idx:idy]):
                    longest = max(len(self.input[idx:idy]), longest)
        return longest


    def compute_recursion(self) -> int:
        """
           Recursively enumerate all possible substrings within a given range, check each one whether or not palindrome
           return right away, else recurse further
           
           solution uses a top-down dynamic programming approach where recursion will continue if memo table not already
           compute max palindromic substring

           time  ~ O(n^2)
           space ~ O(n^2)
        """
        memo = {}
        def recurse(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i,j)]
            
            # we return rather than recurse as any substring within string
            # would be smaller, so doesn't matter if another palindrome is nested here
            if self.is_palindromic(self.input[i:j]):
                memo[(i, j)] = len(self.input[i:j])
                return len(self.input[i:j])

            # If not palindrome, then compute that this string has palindrome len of 0
            # so future computations won't redo computation
            memo[(i, j)] =  0

            left = recurse(i + 1, j) if (i + 1, j) not in memo else memo[(i + 1, j)]
            right = recurse(i, j - 1) if (i, j - 1) not in memo else memo[(i, j - 1)]

            return max(left, right)
        return recurse(0, len(self.input) + 1)

    def compute_recursion_2(self) -> int:
        """
           Recursively enumerate all possible substrings within a given range, check each one whether or not palindrome
           return right away, else recurse further
           
           solution uses a top-down dynamic programming approach where recursion will continue if memo table not already
           compute max palindromic substring

           time  ~ O(n^2)
           space ~ O(n^2)
        """
        from functools import lru_cache
        
        @lru_cache
        def recurse(i: int, j: int) -> int:
            # we return rather than recurse as any substring within string
            # would be smaller, so doesn't matter if another palindrome is nested here
            if self.is_palindromic(self.input[i:j]):
                return len(self.input[i:j])

            left = recurse(i + 1, j)
            right = recurse(i, j - 1)

            return max(left, right)
        return recurse(0, len(self.input) + 1)

    def is_palindromic(self, input: str) -> bool:
        """
            computes whether a given string input is palindromic
        """
        size = len(input)
        if size % 2 == 0:
            substr = int(size/ 2)
            return input[:substr] == input[substr:size+1][::-1]
        
        mid = LongestPalindromicSubstring.math.floor(size/2)
        return input[:mid] == input[mid+1:][::-1]


def main():
    print("Running Main")
    l = LongestPalindromicSubstring("abcdefghijklmnracecaropqrstuvwxyz")
    print(l.compute_recursion())
    print(l.compute_iteration())
    print(l.compute_recursion_2())


if __name__ == '__main__':
    main()

