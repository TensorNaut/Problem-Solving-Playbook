#using dict - hash map
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0:1}

        for num in nums:
            prefix += num
            count += seen.get(prefix%k, 0)
            seen[prefix%k] = seen.get(prefix%k, 0) + 1

        return count
    

# Time Complexity: O(n)
# Space Complexity: O(k)

'''
The idea is to use a hash map to store the count of prefix sums modulo k.
We iterate through the array and calculate the prefix sum. 
For each prefix sum, we check if there is a previous prefix sum that has the same modulo k value. 
If there is, it means that the subarray between those two prefix sums is divisible by k, 
and we can add the count of that prefix sum to our result. 
We also update the count of the current prefix sum modulo k in the hash map.
'''