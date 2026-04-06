def bfs(x: int, y: int, vis: Set[Tuple[int, int]], grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 1
    q =  deque()
    q.append((x, y))
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while q:
        x, y = q.popleft()
        for (dx, dy) in dirs:
            nx, ny = x + dx, y + dy
            if (nx >= 0 and nx < m and ny >= 0 and ny < n) and grid[nx][ny] == 1 and (nx, ny) not in vis:
                res += 1
                vis.add((nx, ny))
                q.append((nx, ny))
    return res

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in vis:
                    vis.add((i, j))
                    area = bfs(i, j, vis, grid)
                    res = max(res, area)
        return res
