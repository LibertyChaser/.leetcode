# @before-stub-for-debug-begin
from python3problem977 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while (left <= right):
            if (nums[left] ** 2 < nums[right] ** 2):
                result = [nums[right] ** 2] + result
                right -= 1
            else:
                result = [nums[left] ** 2] + result
                left += 1
        return result
# @lc code=end

