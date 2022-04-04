from typing import List

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.


'''

class Solution:

    def __init__(self, strs: List[str]) -> None:
        self.strs = strs

    def __repr__(self) -> str:
        buffer = "["
        for s in self.strs:
            buffer += s + ", "
        buffer += "]"

        return buffer
    
    def __len__(self) -> int:
        return len(self.strs)

    def __call__(self) -> str:
        longest_prefix = ""
        starting = self.strs[0]
        stop = False

        for idx, rune in enumerate(starting):
            for str in self.strs:
                try:
                    if rune != str[idx]:
                        stop = True
                except IndexError:
                    stop = True

            if not stop:
                longest_prefix += rune
            else:
                break

        return longest_prefix


def main():
    s = Solution(["flower", "flow", "fl"])
    print(s)
    len(s)
    print(s())

    s2 = Solution(["dog", "racecar", "car"])
    print(s2)
    len(s2)
    print(s2())
    

if __name__ == '__main__':
    main()
      
