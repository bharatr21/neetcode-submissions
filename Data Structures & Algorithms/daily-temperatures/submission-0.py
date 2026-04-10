class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0 for _ in range(n)]
        for idx, temp in enumerate(temperatures):
            while st and st[-1][1] < temp:
                cidx, ctemp = st.pop()
                res[cidx] = idx - cidx 
            st.append((idx, temp))
        return res
