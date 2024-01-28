# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            left = 0
            right = len(nums)
            while (left < right):
                middle = left + (right - left) // 2
                if (nums[middle] < x):
                    left = middle + 1
                else:
                    right = middle
            return left
        
        l = search(target)
        h = search(target + 1) - 1
        if (l <= h):
            return [l, h]
        return [-1, -1]
            

# @lc code=end

