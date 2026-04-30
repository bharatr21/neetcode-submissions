class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        st, en = 0, 0
        res = 0
        fre = defaultdict(int)
        while en < n:
            fre[s[en]] += 1
            while (en - st + 1) - max(fre.values()) > k:
                fre[s[st]] -= 1
                st += 1
            res = max(res, en - st + 1)
            en += 1
        return res
