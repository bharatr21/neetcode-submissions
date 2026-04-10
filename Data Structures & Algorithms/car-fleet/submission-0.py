class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        loc = [(p, s) for p, s in zip(position, speed)]
        loc.sort(key=lambda x: -x[0])
        stk = []
        for p, s in loc:
            stk.append((target - p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)