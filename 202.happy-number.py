# @before-stub-for-debug-begin
from python3problem202 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int):  # -> bool
        record = {}
        cur_sum = 0
        while (True):
            while (n != 0):
                cur_sum += (n % 10) ** 2
                n //= 10
            if cur_sum == 1:
                return True
            if cur_sum in record:
                return False
            record[cur_sum] = 1
            n = cur_sum
            cur_sum = 0
        
# @lc code=end

