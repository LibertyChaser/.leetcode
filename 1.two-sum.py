# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int): # -> List[int]:
        record = dict()
        for index, value in enumerate(nums):
            if target - value in record:
                return [record[target - value], index]
            record[value] = index
        return []
# @lc code=end

