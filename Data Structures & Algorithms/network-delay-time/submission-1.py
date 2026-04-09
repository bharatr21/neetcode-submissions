class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for info in times:
            src, dst, cost = info
            adj[src].append((cost, dst))
        pq = []
        vis = set()
        heapq.heappush(pq, (0, k))
        res = 0
        while pq and len(vis) < n:
            cost, cur = heapq.heappop(pq)
            if cur in vis:
                continue
            vis.add(cur)
            res = cost
            for (edge_cost, neigh) in adj[cur]:
                if neigh not in vis:
                    heapq.heappush(pq, (cost + edge_cost, neigh))

        return res if len(vis) == n else -1