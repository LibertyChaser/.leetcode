# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        size = len(nums)
        if (sum(nums) < target):
            return 0
        result = len(nums) + 1
        curr_sum = 0
        while (fast < size):
            curr_sum += nums[fast]
            while (curr_sum >= target):
                result = min(result, fast - slow + 1)
                curr_sum -= nums[slow]
                slow += 1
                
            fast += 1
                    
        return result
# @lc code=end

