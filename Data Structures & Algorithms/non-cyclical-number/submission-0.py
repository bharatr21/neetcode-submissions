def sumSq(n: int) -> int:
    res = 0
    while n:
        res += (n % 10) ** 2
        n = n // 10
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            seen.add(n)
            print(n)
            n = sumSq(n)
            if n in seen and n != 1:
                return False
            elif n == 1:
                return True
