# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int): # -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # pri_que = []  # 小顶堆

        # # 用固定大小为k的小顶堆，扫描所有频率的数值
        # for key, freq in map_.items():
        #     heapq.heappush(pri_que, (freq, key))
        #     if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
        #         heapq.heappop(pri_que)

        # # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        # result = [0] * k
        # for i in range(k-1, -1, -1):
        #     result[i] = heapq.heappop(pri_que)[1]
        # return result
    
        pri_que = PriorityQueue()
        for key, freq in map_.items():
            pri_que.put((freq, key))
            if pri_que.qsize() > k:
                pri_que.get()

        return [pri_que.get()[1] for _ in range(k)]
# @lc code=end

