# @before-stub-for-debug-begin
from python3problem844 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            slow = []
            fast = 0
            size = len(s)
            while (fast < size):
                if (s[fast] != "#"):
                    slow += [s[fast]]
                else:
                    slow = slow[:-1]
                fast += 1
            return slow
        
        return backspace(s) == backspace(t)
# @lc code=end

