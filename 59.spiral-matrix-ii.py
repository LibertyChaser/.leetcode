# @before-stub-for-debug-begin
from python3problem59 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        offset = 0
        filling = 1
        result = []
        mid = n // 2
        for i in range(n):
            result.append([0] * n)
        
        while (offset <= mid):
            
            for i in range(offset, n - offset - 1):
                result[offset][i] = filling
                filling += 1
            for i in range(offset, n - offset - 1):
                result[i][n - offset - 1] = filling
                filling += 1
            for i in range(n - offset - 1, offset, -1):
                result[n - offset - 1][i] = filling
                filling += 1
            for i in range(n - offset - 1, offset, -1):
                result[i][offset] = filling
                filling += 1
            offset += 1
        
        if (n % 2 == 1):
            result[mid][mid] = filling
            
        return result
            
# @lc code=end

