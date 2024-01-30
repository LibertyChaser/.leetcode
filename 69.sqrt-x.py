#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int):# -> int:
        if x == 1:
            return 1
        left = 1
        right = x // 2 + 1
        while (left < right):
            middle = left + (right - left) // 2
            if middle ** 2 == x:
                return middle
            if middle ** 2 < x:
                left = middle + 1
            else:
                right = middle
        return left - 1
                
# @lc code=end

