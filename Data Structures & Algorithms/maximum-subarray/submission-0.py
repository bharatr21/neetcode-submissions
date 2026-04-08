class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            sub_sum = max(sub_sum + nums[i], nums[i])
            max_sum = max(max_sum, sub_sum)
        return max_sum