# @before-stub-for-debug-begin
from python3problem35 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while (left < right):
            middle = left + (right - left) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle
            elif (nums[middle] < target):
                left = middle + 1
        return left
# @lc code=end

