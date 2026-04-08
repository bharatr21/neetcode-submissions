from functools import lru_cache

@lru_cache
def solve(n: int) -> int:
    if n == 1: return 1
    elif n == 2: return 2
    else:
        return solve(n - 1) + solve(n - 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        return solve(n)   