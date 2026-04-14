def solve(nums: List[int], target: int, tmp: List[int], res: set[tuple[int]]):
    if target < 0: return
    elif target == 0:
        test = tuple(sorted(tmp.copy()))
        if test not in res:
            res.add(test)
        return
    else:
        for n in nums:
            if n <= target:
                tmp.append(n)
                solve(nums, target - n, tmp, res)
                tmp.pop()

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        tmp = []
        nums.sort()
        solve(nums, target, tmp, res)
        return [list(x) for x in list(res)]