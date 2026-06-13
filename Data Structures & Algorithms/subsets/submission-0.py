from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        for i in range(1, n+1):
            res.extend([list(c) for c in combinations(nums, i)])

        return res