class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn_so_far = max(prices)
        res = 0
        for price in prices:
            mn_so_far = min(mn_so_far, price)
            res = max(res, price - mn_so_far)

        return res