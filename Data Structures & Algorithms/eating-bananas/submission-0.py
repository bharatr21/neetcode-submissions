def duration(k: int, piles: List[int]) -> int:
    res = 0
    for qty in piles:
        res += math.ceil(qty / k)
    return res

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        if h == len(piles): return right
        while left <= right:
            mid = left + ((right - left) // 2)
            d = duration(mid, piles)
            if d <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left