class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in a and a[s[r]] >= l:
                l = a[s[r]] + 1
            a[s[r]] = r
            res = max(res, r - l + 1)
        return res


            