class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inft = float("inf")
        prices = [inft] * n
        prices[src] = 0
        for _ in range(k+1):
            tmp = prices.copy()
            for csrc, cdst, cost in flights:
                if prices[csrc] == inft:
                    continue
                if prices[csrc] + cost < tmp[cdst]:
                    tmp[cdst] = prices[csrc] + cost
            prices = tmp

        return -1 if prices[dst] == inft else prices[dst]