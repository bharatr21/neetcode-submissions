class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.pq = stones
        heapq.heapify_max(self.pq)
        while len(self.pq) > 1:
            y, x = heapq.heappop_max(self.pq), heapq.heappop_max(self.pq)
            if x < y:
                heapq.heappush_max(self.pq, y - x)
        return 0 if not self.pq else self.pq[0]