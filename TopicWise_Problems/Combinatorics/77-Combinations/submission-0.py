from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        return list(combinations(arr, k))
    

# Time Complexity: O(k * C(n, k)) where C(n, k) is the number of combinations.
# Space Complexity: O(k * C(n, k)) for storing the output list of combinations
'''
The code defines a class `Solution` with a method `combine` that generates all possible combinations 
of `k` numbers from the range 1 to `n`. It uses the `combinations` function from the `itertools` module 
to generate the combinations efficiently. The time complexity is O(k * C(n, k)) because generating each 
combination takes O(k) time, and there are C(n, k) combinations in total. The space complexity is also 
O(k * C(n, k)) for storing the output list of combinations.
'''