#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # using dictionary to record
        # record = {}
        # for i in nums1:
        #     record[i] = 1
        # result = []
        # for i in nums2:
        #     if i in record:
        #         result += [i]
        #         del record[i]
        # return result
        # using array
        # record1 = [0] * 1001
        # record2 = [0] * 1001
        # result = []
        # for i in nums1:
        #     record1[i] = 1
        # for i in nums2:
        #     record2[i] = 1
        # for i in range(1001):
        #     if record1[i] != 0 and record2[i] != 0:
        #         result += [i]
        # return result
        # using set
        return list(set(nums1) & set(nums2))
    
# @lc code=end

