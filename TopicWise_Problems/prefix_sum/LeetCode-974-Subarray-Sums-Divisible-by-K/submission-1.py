#using defaultdict - hash map
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = prefix = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            prefix += num
            rem = prefix % k
            count += seen[rem]
            seen[rem] += 1

        return count