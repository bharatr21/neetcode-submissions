def solve(nums: List[int], dp: List[bool]) -> bool:
    n = len(nums)
    for i in range(n-2, -1, -1):
        for jump in range(nums[i] + 1):
            if i + jump >= n - 1 or dp[i + jump]:
                dp[i] = True
                break

    return dp[0]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        return solve(nums, dp)
