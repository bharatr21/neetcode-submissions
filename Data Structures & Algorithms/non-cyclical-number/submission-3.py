def sumSq(n: int) -> int:
    res = 0
    while n:
        res += (n % 10) ** 2
        n //= 10
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sumSq(n)
            if n == 1:
                return True
        return False
