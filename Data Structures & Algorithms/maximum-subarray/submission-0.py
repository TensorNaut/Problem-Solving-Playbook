#bruteforce

import heapq
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        h = []
        n = len(nums)
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                heapq.heappush(h, -summ)
        return -heapq.heappop(h)