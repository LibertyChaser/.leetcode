# @before-stub-for-debug-begin
from python3problem283 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        size = len(nums)
        
        while (fast < size):
            if (nums[fast] != 0):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while (slow < size):
            nums[slow] = 0
            slow += 1
            
        return nums
        
# @lc code=end

