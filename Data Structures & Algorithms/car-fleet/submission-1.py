class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        loc = [(p, s) for p, s in zip(position, speed)]
        loc.sort(reverse=True)
        stk = []
        for p, s in loc:
            stk.append((target - p) / s)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)