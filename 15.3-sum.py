# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]): # -> List[List[int]]:
        # Loop Sliding Window
        nums.sort()
        size = len(nums)
        result = set()
        for i in range(size - 2): 
            if nums[i] > 0:
                break
            left = i + 1
            right = size - 1
            while (left < right):
                if nums[right] < 0:
                    break
                if nums[left] + nums[right] == - nums[i]:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[left] + nums[right] > - nums[i]:
                    right -= 1
                else:
                    left += 1
        return result
    
        # Accepted
        # 312/312 cases passed (1732 ms)
        # Your runtime beats 18.87 % of python3 submissions
        # Your memory usage beats 86.81 % of python3 submissions (20.4 MB)
    
        # Loop and 2Sum
        # result = set()
        # size = len(nums)
        # for i in range(size - 2):
        #     record = dict()
        #     for j in range(i + 1, size):
        #         if - nums[j] in record:
        #             result.add(tuple(sorted([nums[i], nums[j], - nums[i] - nums[j]])))
        #             del record[- nums[j]]
        #         else:
        #             record[nums[i] + nums[j]] = 1
        # return result
        # Accepted
        # 312/312 cases passed (2289 ms)
        # Your runtime beats 12.11 % of python3 submissions
        # Your memory usage beats 44.65 % of python3 submissions (21.4 MB)
    
        # Double for loop with Dictionary, TLE
        # size = len(nums)
        # record = {}
        # result = set()
        # z_num = 0
        # for i in range(1, size):
        #     for j in range(i):
        #         if nums[i] + nums[j] in record:
        #             record[nums[i] + nums[j]] += [[nums[i], nums[j]]]
        #         else:
        #             record[nums[i] + nums[j]] = [[nums[i], nums[j]]]
        # for i in range(size):
        #     if -nums[i] in record:
        #         for lst in record[-nums[i]]:
        #             if nums[i] not in lst:
        #                 result.add(tuple(sorted(lst + [nums[i]])))
        # for num in nums:
        #     if num == 0:
        #         z_num += 1
        # if z_num >= 3:
        #     result.add((0, 0, 0))
        # return result
        
        
        # Loop Binary Search TLE
        # def search(target, left):
        #     right = len(nums)
        #     while (left < right):
        #         middle = left + (right - left) // 2
        #         if nums[middle] == target:
        #             return middle
        #         if nums[middle] > target:
        #             right = middle
        #         else:
        #             left = middle + 1
        #     return -1
        
        # result = set()
        # size = len(nums)
        # nums.sort()
        
        # for i in range(size - 2):
        #     if nums[i] > 0:
        #         break
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, size - 1):
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #         if -nums[i]-nums[j] < nums[j]:
        #             break
        #         k = search(target=-nums[i]-nums[j], left=j+1)
        #         if k != -1:
        #             result.add((nums[i], nums[j], nums[k]))
        # return result
        

# @lc code=end

