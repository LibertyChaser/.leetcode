#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]): # -> None:
        """
        Do not return anything, modify s in-place instead.
        plz LOOOK AT HERE
        """
        # Library Function
        # s.reverse()
        
        # Double Pointers
        # right = len(s) - 1
        # left = 0
        # while (left < right):
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        # Range
        # size = len(s)
        # for i in range(size // 2): # 这里的 size // 2 非常有意思
        #     s[i], s[- 1 - i] = s[- 1 - i], s[i]
    
        # Slicing
        s[:] = s[:: -1]
# @lc code=end

