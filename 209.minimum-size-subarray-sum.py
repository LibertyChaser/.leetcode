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
    def minSubArrayLen(self, target: int, nums: List[int]): # -> int:
        slow = 0
        size = len(nums)
        result = size + 1
        curr_sum = 0
        for i in range(size):
            curr_sum += nums[i]
            while (curr_sum >= target):
                result = min(result, i - slow + 1)
                curr_sum -= nums[slow]
                slow += 1
                    
        return result if result != size + 1 else 0
# @lc code=end

