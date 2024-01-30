# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        size = len(nums)
        while (fast < size):
            temp = nums[slow]
            if (nums[fast] == temp):
                fast += 1
            else: 
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
# @lc code=end

