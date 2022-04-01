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

    def __init__(self, strs: List[str]) -> str:
        self.strs = strs

    def __repr__(self) -> str:
        cache = "["
        for s in self.strs:
            cache += s + ", "
        cache += "]"
        return cache
    
    def __len__(self) -> int:
        return len(self.strs)




def main():
    s = Solution(["flower", "flow", "flight"])
    print(s)
    len(s)
    

if __name__ == '__main__':
    main()
      
