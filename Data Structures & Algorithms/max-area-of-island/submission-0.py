def dfs(x: int, y: int, vis: Set[Tuple[int, int]], grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    mx = 1
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for (dx, dy) in dirs:
        nx, ny = x + dx, y + dy
        if (nx >= 0 and nx < m and ny >= 0 and ny < n) and grid[nx][ny] == 1 and (nx, ny) not in vis:
            vis.add((nx, ny))
            mx = max(mx, 1 + dfs(nx, ny, vis, grid))
    return mx


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in vis:
                    vis.add((i, j))
                    sz = dfs(i, j, vis, grid)
                    res = max(res, sz)
        return res
