from functools import lru_cache

@lru_cache
def solve(m: int, n: int) -> int:
    if m == 0 or n == 0: return 1
    return solve(m, n - 1) + solve(m - 1, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return solve(m - 1, n - 1)