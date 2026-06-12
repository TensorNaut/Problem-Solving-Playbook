from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        for i in range(1, n+1):
            res.extend(list(combinations(nums, i)))

        return res

# Time Complexity: O(k * C(n, k)) where C(n, k) is the number of combinations for each k from 1 to n.
# Space Complexity: O(k * C(n, k)) for storing the output list of subsets
'''
The code defines a class `Solution` with a method `subsets` that generates all possible subsets of a 
given list of numbers `nums`. It uses the `combinations` function from the `itertools` module to generate 
combinations of different lengths (from 1 to n) and extends the result list with these combinations. 
The time complexity is O(k * C(n, k)) because generating each combination takes O(k) time, 
and there are C(n, k) combinations for each k from 1 to n. The space complexity is also O(k * C(n, k)) 
for storing the output list of subsets.
'''