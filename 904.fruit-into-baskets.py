# @before-stub-for-debug-begin
from python3problem904 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]): # -> int:
        slow = 0
        result = 0
        record = {}
        size = len(fruits)
        for i in range(size):
            record[fruits[i]] = record.get(fruits[i], 0) + 1
            while (len(record) > 2):
                record[fruits[slow]] = record.get(fruits[slow], 0) - 1
                if record[fruits[slow]] == 0:
                    del record[fruits[slow]]
                slow += 1

            result = max(result, i - slow + 1)
        return result
# @lc code=end

