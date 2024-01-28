# @before-stub-for-debug-begin
from python3problem704 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = left + (right - left) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle - 1
            elif (nums[middle] < target):
                left = middle + 1
        return -1
        # left = 0
        # right = len(nums)
        # while (left < right):
        #     middle = (left + right) // 2
        #     if (nums[middle] == target):
        #         return middle
        #     elif (nums[middle] > target):
        #         right = middle
        #     elif (nums[middle] < target):
        #         left = middle + 1
        # return -1
            

        
# @lc code=end
