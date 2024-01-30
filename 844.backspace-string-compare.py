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
            size = len(s)
            result = []
            for i in range(size):
                if (s[i] != "#"):
                    result.append(s[i])
                else:
                    result = result[:-1]
            return result

        return backspace(s) == backspace(t)
# @lc code=end

