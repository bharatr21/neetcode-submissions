class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, en = 0, 0
        n = len(s)
        mp = defaultdict(int)
        res = 0
        d = 0
        while en < n:
            mp[s[en]] += 1
            if mp[s[en]] == 2: d += 1
            while d > 0:
                mp[s[st]] -= 1
                if mp[s[st]] == 1: d -= 1
                st += 1

            res = max(res, en - st + 1)
            en += 1
        return res