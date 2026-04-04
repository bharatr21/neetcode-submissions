class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        seen = set()
        mx_l = 0
        for el in uniq:
            if el in seen:
                continue
            while (el - 1) in uniq: # Find start of sequence
                el -= 1

            st = el
            cur_l = 0
            while st in uniq:
                seen.add(st)
                st += 1
                cur_l += 1
            mx_l = max(mx_l, cur_l)

        return mx_l
