#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str): # -> str:
        res = list()
        for char in s:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)
        return "".join(res)
# @lc code=end

