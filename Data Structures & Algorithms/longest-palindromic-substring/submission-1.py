class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"            # "aba" → "#a#b#a#"
        n = len(t)
        p = [0] * n
        l = r = 0                              # the farthest-right palindrome so far

        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[l + (r - i)])   # start from the mirror's answer
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < n
                   and t[i - p[i] - 1] == t[i + p[i] + 1]):
                p[i] += 1                      # expand only beyond what's known
            if i + p[i] > r:                   # reaches farther right → new [l, r]
                l, r = i - p[i], i + p[i]

        length, center = max((v, i) for i, v in enumerate(p))
        start = (center - length) // 2         # convert back to an index in s
        return s[start:start + length]


# remember what is already done