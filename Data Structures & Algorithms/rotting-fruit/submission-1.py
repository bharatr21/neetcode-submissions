class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        fre = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fre += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fre:
            r, c, time = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < m and nc >= 0 and nc < n) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, time + 1))
                    res = max(res, time + 1)
                    fre -= 1
        
        return res if not fre else -1