#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int): # -> str:
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s
        
# @lc code=end

