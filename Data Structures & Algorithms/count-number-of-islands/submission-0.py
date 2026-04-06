def inBound(x: int, y: int, m: int, n: int) -> bool:
    return (x >= 0 and x < m and y >= 0 and y < n)

def dfs(x: int, y: int, vis: Set[Tuple[int, int]], grid: List[List[str]]) -> None:
    vis.add((x, y))
    m, n = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for (dx, dy) in dirs:
        nx, ny = x + dx, y + dy
        if inBound(nx, ny, m, n) and grid[nx][ny] == '1' and (nx, ny) not in vis:
            dfs(nx, ny, vis, grid)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        vis = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in vis:
                    res += 1
                    dfs(i, j, vis, grid)
        return res
