#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str): # -> bool:
        def construct(s):
            record = [0] * 26
            for char in s:
                record[ord(char) - ord("a")] += 1
            return record
        record1 = construct(ransomNote)
        record2 = construct(magazine)
        for i in range(26):
            if record1[i] > record2[i]:
                return False
        return True
# @lc code=end

