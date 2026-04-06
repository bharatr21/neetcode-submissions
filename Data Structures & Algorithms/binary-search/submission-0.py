from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = bisect_left(nums, target)
        return a if nums[a] == target else -1