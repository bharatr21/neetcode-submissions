class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        cur = newInterval
        for i in range(len(intervals)):
            st, en = intervals[i]
            cur_st, cur_en = cur
            if cur_en < st:
                res.append(cur)
                return res + intervals[i:]
            elif cur_st > en:
                res.append(intervals[i])
            else:
                cur = [min(cur_st, st), max(cur_en, en)]

        res.append(cur)
        return res