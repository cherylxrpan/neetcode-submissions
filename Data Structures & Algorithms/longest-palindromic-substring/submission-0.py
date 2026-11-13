class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1                   # step outward
                r += 1
            return s[l + 1:r]            # the last window that matched

        for i in range(len(s)):
            odd = expand(i, i)           # center on one letter
            even = expand(i, i + 1)      # center between two letters
            res = max(res, odd, even, key=len)
        return res
        