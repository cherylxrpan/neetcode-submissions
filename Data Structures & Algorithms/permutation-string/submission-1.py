class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        window = {}
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if r-l+1>k:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]] 
                l += 1
            
            if window == need:
                return True
        return False

            