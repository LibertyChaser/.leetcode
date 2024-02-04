#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str): # -> str:
        # strip()
        # s = s.strip()
        # s = s[::-1]
        # s = ' '.join(word[::-1] for word in s.split())
        # return s
    
        # Double Pointers
        words = s.split()
        left = 0
        right = len(words) - 1
        while (left < right):
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)
# @lc code=end

