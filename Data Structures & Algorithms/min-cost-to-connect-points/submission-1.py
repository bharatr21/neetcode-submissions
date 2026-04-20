import heapq

def mdist(pt1: Tuple[int], pt2: Tuple[int]) -> int:
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        seen = [False] * n
        dist = [100000000] * n
        pq = []
        e, res = 0, 0
        while e < n - 1:
            seen[node] = True
            nex = -1
            for i in range(n):
                if seen[i]:
                    continue
                cur = mdist(points[node], points[i])
                dist[i] = min(cur, dist[i])
                if nex == -1 or dist[i] < dist[nex]:
                    nex = i

            e += 1
            res += dist[nex]
            node = nex
        return res
