#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str): # -> str:
        # res = list()
        # for char in s:
        #     if res and res[-1] == char:
        #         res.pop()
        #     else:
        #         res.append(char)
        # return "".join(res)
        left = 0
        right = 0
        size = len(s)
        res = list(s)
        while (right < size):
            res[left] = res[right]
            if left > 0 and res[left] == res[left - 1]:
                left -= 1
            else:
                left += 1
            right += 1
        return "".join(res[:left])
# @lc code=end

