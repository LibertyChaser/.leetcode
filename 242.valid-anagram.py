#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def anagram(s):
            result = [0] * 26
            for char in s:
                result[ord(char) - ord("a")] += 1
            return result
        return anagram(s) == anagram(t)
# @lc code=end

