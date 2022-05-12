# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
# 
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
# 
#
# Constraints:
#
#     1 <= nums.length <= 104
#     0 <= nums[i] <= 1000

from typing import List

class MinimizeJumps:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
    
    def __call__(self, strategy: str) -> int:
        import logging
        try:
            return getattr(self, strategy)()
        except AttributeError:
            logging.getLogger().error(f'incorrect strategy: \"{strategy}\" selected, defaulting to slow!')
            return self.compute_slow()
    
    def compute_slow(self) -> int:
        """
            top-down recursion with a priority_queue
           
            solution recursively enumerates over all possible hops from a given
            current_idx and keeps track of the following information: "hops it took to reach there"
            which is represented as a summation of unsigned integers (1)

            once recursion reaches a termination condition, we potentially record the summation of unsiqned integers
            thus far in a priority queue which will prioritize based on 

            time  ~  O()
            space ~  O()
            
        """
        from queue import PriorityQueue
        buffer = PriorityQueue()

        def recurse(current_idx, hops) -> None:
            # hop is considered invalid, we do not record
            if current_idx > len(self.nums) - 1:
                return

            # hop is considered valid and successful, we record 
            if current_idx == len(self.nums) - 1:
                buffer.put((hops, (current_idx, hops)))
                return
            
            # top-down recursion here
            val = self.nums[current_idx]
            while val > 0:
                recurse(current_idx + val, hops + 1)
                val -= 1

        recurse(0, 0)
        return buffer.get()[0]


    def compute_fast(self) -> int:
        """
            top-down recursion with cache for quick lookup

            idea is to relate solutions to sub-problems as the solution to overall problem
            1 + ...
        
        """
        from functools import cache

        @cache
        def recurse(current_idx: int) -> int:
            if current_idx == len(self.nums) - 1:
                return 0
            
            hops = list()
            for scalar in range(1, self.nums[current_idx] + 1):
                if scalar + current_idx <= len(self.nums) - 1:
                    hops.append(1 + recurse(scalar + current_idx))
            return min(hops) if hops else 100

        return recurse(0)


def main():
    #print(MinimizeJumps([2, 3, 1, 1, 4])())
    from random import randint
    game_state = [randint(1, 5) for x in range(1, 23)]
    print(game_state)
    print(MinimizeJumps(game_state)('compute_quick'))
    print(MinimizeJumps(game_state)('compute_fast'))

if __name__ == '__main__':
    main()
