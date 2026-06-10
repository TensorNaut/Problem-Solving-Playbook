class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)

        for i, val in enumerate(nums):
            rightsum -= val
            if leftsum == rightsum:
                return i
            leftsum += val
            
        return -1
            

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
The idea is to use two variables, leftsum and rightsum, 
to keep track of the sum of the elements to the left and right of the current index, respectively.

We initialize leftsum to 0 and rightsum to the sum of all elements in the array.
We iterate through the array and for each element, we update rightsum by subtracting the current element from it. 
Then we check if leftsum is equal to rightsum. If they are equal, it means that the current index is the pivot index,
and we return it.
If they are not equal, we update leftsum by adding the current element to it and continue to the next index.
If we finish iterating through the array and do not find a pivot index, we return -1.
'''