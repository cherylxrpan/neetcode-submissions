class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        missing = len(t)
        l = 0
        best = (float('inf'), 0, 0) # length, start, end

        for r, ch in enumerate(s):
            if need[ch]>0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if r-l+1<best[0]:
                    best = (r - l + 1, l, r + 1)

                need[s[l]] += 1              # give back s[l]
                if need[s[l]] > 0:       
                    missing += 1
                l += 1
                
        return "" if best[0] == float('inf') else s[best[1]:best[2]]