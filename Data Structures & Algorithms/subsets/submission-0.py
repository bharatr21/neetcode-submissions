def solve(idx, nums: List[int], tmp: List[int], res: List[List[int]]):
    n = len(nums)
    if idx == n:
        res.append(tmp.copy())
        return

    else:
        tmp.append(nums[idx])
        solve(idx + 1, nums, tmp, res)
        tmp.pop()
        solve(idx + 1, nums, tmp, res)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        solve(0, nums, tmp, res)
        return res