class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inft = float("inf")
        prices = [inft] * n
        prices[src] = 0
        adj = defaultdict(list)
        for s, d, cost in flights:
            adj[s].append((d, cost))
        
        q = deque([(0, src, 0)])
        while q:
            cost, node, stops = q.popleft()
            if stops > k: 
                continue
            
            for neigh, w in adj[node]:
                newCost = cost + w
                if newCost < prices[neigh]:
                    prices[neigh] = newCost
                    q.append((newCost, neigh, stops + 1))

        return -1 if prices[dst] == inft else prices[dst]