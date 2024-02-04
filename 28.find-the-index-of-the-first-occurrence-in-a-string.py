#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    # def getNext(self, next, s):
    #     j = 0
    #     next[0] = 0
    #     for i in range(1, len(s)):
    #         while j > 0 and s[i] != s[j]:
    #             j = next[j - 1]
    #         if s[i] == s[j]:
    #             j += 1
    #         next[i] = j
    
    def strStr(self, haystack: str, needle: str): # -> int:
        # if len(needle) == 0:
        #     return 0
        # next = [0] * len(needle)
        # self.getNext(next=next, s=needle)
        # j = 0
        # for i in range(len(haystack)):
        #     while j > 0 and haystack[i] != needle[j]:
        #         j = next[j - 1]
        #     if haystack[i] == needle[j]:
        #         j += 1
        #     if j == len(needle):
        #         return i - len(needle) + 1
        # return -1
        
        # Lib Func - find()
        # return haystack.find(needle)

        # Lib Func - index
        try:
            return haystack.index(needle)
        except ValueError:
            return - 1
        

# @lc code=end

