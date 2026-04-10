class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            heapq.heappush_max(pq, (x**2 + y**2, x, y))
            if len(pq) > k:
                heapq.heappop_max(pq)
        return [[x, y] for _, x, y in pq]