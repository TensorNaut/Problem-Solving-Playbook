import math
import heapq

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        heapq.heapify(nums)

        gcd = math.gcd(*numsDivide)
        k = 0

        while nums and gcd%nums[0] != 0:
            k += 1
            heapq.heappop(nums)

        return -1 if not nums else k
    

'''
Time Complexity: O(nlogn + m) where n is the length of the input list nums and m is the length 
of the input list numsDivide. The heapify operation takes O(n) time, and in the worst case, 
we may need to pop all elements from the heap, which takes O(nlogn) time. The gcd calculation takes O(m) time.

Space Complexity: O(n) as we are using a heap to store the elements of the input list nums.
'''
