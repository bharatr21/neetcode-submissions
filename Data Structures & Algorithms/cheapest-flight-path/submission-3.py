class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inft = float("inf")
        prices = [inft] * n
        prices[src] = 0
        adj = defaultdict(list)
        for s, d, cost in flights:
            adj[s].append((d, cost))
        
        pq = [(0, src, 0)]
        while pq:
            cost, node, stops = heapq.heappop(pq)
            if node == dst:
                return cost
            if stops > k: 
                continue
            
            for neigh, w in adj[node]:
                heapq.heappush(pq, (cost + w, neigh, stops + 1))

        return -1 if prices[dst] == inft else prices[dst]