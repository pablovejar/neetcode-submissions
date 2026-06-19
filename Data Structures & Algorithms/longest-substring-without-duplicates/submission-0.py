class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in longestSub:
                longestSub.remove(s[l])
                l += 1
            longestSub.add(s[r])
            res = max(res, r-l+1)

        return res
        