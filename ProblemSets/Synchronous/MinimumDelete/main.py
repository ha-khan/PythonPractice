# A string s is called good if there are no two different characters in s that have the same frequency.
#
# Given a string s, return the minimum number of characters you need to delete to make s good.
#
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
#
# 
#
# Example 1:
#
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
#
# Example 2:
#
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
#
# Example 3:
#
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
#
# 
#
# Constraints:
#
#     1 <= s.length <= 105
#     s contains only lowercase English letters.
from itertools import count
from typing import Iterable


class MinimumDelete:
    def __init__(self, s: str):
        self.s = s

    def _solution_0(self) -> int:
        """
            Problem doesn't specify need to preserve the string

            we can apply pre-processing to the string and sort it which would 

            give us structure that conveys information that would we can use.

            Sorting groups 'exact' or 'similar' elements together

            time  ~ O(nlog), sorting of string chars 
            space ~ O(N), 
        """

        deleted = 0
        sorted_s = sorted(self.s)

        current_rune = sorted_s[0]
        count = set()
        counter = 0
        for rune in sorted_s:
            if rune != current_rune:
                current_rune = rune
                diff_counter = counter
                # check if need to delete
                while counter in count and counter > 0:
                    counter = counter - 1
                    # print(diff_counter, counter)
                # keep track of amount deleted 
                count.add(counter)
                deleted += (diff_counter - counter)
                counter = 1 
            else:
                counter += 1

        diff_counter = counter
        # check if need to delete
        while counter in count and counter > 0:
            counter = counter - 1
            # print(diff_counter, counter)
        # keep track of amount deleted 
        count.add(counter)
        deleted += (diff_counter - counter)
        
        return deleted
    
    def _solution_1(self) -> int:
        """
            This solution optimizes 
        """
        sorted_runes = sorted(self.s)
        count_of_runes = set()
        current_rune = sorted_runes[0]
        deleted = 0

        def helper(counter) -> int:
            """
                helper helps with double iterator 
            """
            removed = counter
            while counter > 0 and counter in count_of_runes:
                counter -= 1
            
            count_of_runes.add(counter)
            return removed - counter

        counter = 0
        for rune in sorted_runes:
            if rune != current_rune:
                deleted += helper(counter)
                counter = 1
                current_rune = rune
            else:
                counter += 1
        deleted += helper(counter)

        return deleted
        
    def __call__(self, *args, **kwargs) -> int:
        try:
            fn = getattr(self, args[0])
        except (AttributeError, IndexError) as e:
            return self._solution_0()
        
        return fn()


def main():
    s = MinimumDelete("abcabcabcd")
    print(s())


if __name__ == '__main__':
    main()
