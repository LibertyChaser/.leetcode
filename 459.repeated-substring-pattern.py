#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str): # -> bool:
        size = len(s)
        next = [0] * size
        self.getNext(next=next, s=s)
        if next[-1] != 0 and size % (size - next[-1]) == 0:
            return True
        return False
            
        
    def getNext(self, next, s):
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
            
        
# @lc code=end

