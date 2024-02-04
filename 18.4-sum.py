#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int): # -> List[List[int]]:
        # Loop Sliding Windows
        nums.sort()
        size = len(nums)
        result = set()
        for i in range(size - 3):
            for j in range(i + 1, size - 2):
                left  = j + 1
                right = size - 1
                while (left < right):
                    if nums[left] + nums[right] == target - nums[j] - nums[i]:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                    elif nums[left] + nums[right] < target - nums[j] - nums[i]:
                        left += 1
                    else:
                        right -=1
        return result
                    
# @lc code=end

