from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for el in nums:
            freq[el] += 1
        res = [(el, freq[el]) for el in freq]
        res = sorted(res, key=lambda x: -x[1])
        return [el[0] for el in res][:k]