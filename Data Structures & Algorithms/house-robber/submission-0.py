from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache
        def solve(idx: int) -> int:
            if idx < 0: return 0
            if idx == 0: return nums[0]
            elif idx == 1: return max(nums[0], nums[1])
            return max(solve(idx - 1), nums[idx] + solve(idx - 2))
        
        return solve(n - 1)