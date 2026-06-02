from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict(sorted(Counter(nums).items(), key=lambda item:item[1], reverse=True))
        res = [i for i, v in freq.items()]
        return res[:k]