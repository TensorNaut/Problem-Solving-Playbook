import math
from collections import deque

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums = deque(sorted(nums))

        gcd = math.gcd(*numsDivide)
        k = 0

        while nums and gcd%nums[0] != 0:
            k += 1
            nums.popleft()

        return -1 if not nums else k
    

'''
Time Complexity: O(nlogn + m) where n is the length of the input list nums and m is the length
of the input list numsDivide. The sorting operation takes O(nlogn) time, and in the worst case,
we may need to pop all elements from the deque, which takes O(n) time. The gcd calculation takes O(m) time.

Space Complexity: O(n) as we are using a deque to store the elements of the input list nums.
'''
