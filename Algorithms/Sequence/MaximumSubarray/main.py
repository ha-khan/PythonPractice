"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""
from typing import List

class MaximumSubarray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.largest = 0 

    def compute_slow(self) -> int:
        '''
        Uses two iterators 
            time  ~ O(n^2)
            space ~ O(1) 
        '''
        for idx, _ in enumerate(self.nums):
            for idy in range(idx, len(self.nums) + 1):
                if self.largest < sum(self.nums[idx:idy]):
                    self.largest = sum(self.nums[idx:idy])
        return self.largest


def main():
    m = MaximumSubarray([4, -1, 2, 1])
    print(m.compute_slow())


if __name__ == '__main__':
    main()
