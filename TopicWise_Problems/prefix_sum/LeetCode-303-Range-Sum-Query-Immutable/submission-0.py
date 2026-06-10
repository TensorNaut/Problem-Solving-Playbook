class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        for i in range(1 ,n):
            nums[i] = nums[i-1] + nums[i]
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:    
            return self.nums[right] - self.nums[left -1]



# Time Complexity: O(n)
# Space Complexity: O(n)
'''
The constructor of the NumArray class takes an input array nums and 
modifies it in-place to store the prefix sums.

The sumRange method then uses these prefix sums to calculate the sum of 
the elements between the left and right indices in constant time.

The prefix sum at index i (nums[i]) represents the sum of all elements from 
index 0 to index i in the original array.

To calculate the sum of elements between left and right, 
we can use the formula:
sumRange(left, right) = nums[right] - nums[left - 1] if left > 0 else nums[right]

This allows us to efficiently compute the range sum in O(1) time after an O(n) 
preprocessing step in the constructor.'''
