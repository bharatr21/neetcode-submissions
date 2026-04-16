class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stk = []
        for i in range(n+1):
            while stk and (i == n or heights[i] <= heights[stk[-1]]):
                ht = heights[stk.pop()]
                width = i - stk[-1] - 1 if stk else i
                res = max(res, ht * width)
            stk.append(i)
        return res
