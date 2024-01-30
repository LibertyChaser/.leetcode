# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]): # -> List[int]:
        offset = 0
        m = len(matrix)
        n = len(matrix[0])
        result = []
        if m == 1:
            return matrix[0]
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        while (min(m, n) // 2 >= offset):
            for i in range(offset, n - offset - 1):
                result.append(matrix[offset][i])
            for i in range(offset, m - offset - 1):
                result.append(matrix[i][n - 1 - offset])
            for i in range(n - 1 - offset, offset, -1):
                result.append(matrix[m - 1 - offset][i])
            for i in range(m - 1 - offset, offset, -1):
                result.append(matrix[i][offset])
            offset += 1
        if m == n and n % 2 == 1:
            result.append(matrix[m //2][m // 2])
        return result
# @lc code=end

