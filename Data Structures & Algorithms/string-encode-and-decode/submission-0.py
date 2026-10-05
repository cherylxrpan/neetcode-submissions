class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += (str(len(s)) + '#' + s) 
        return output
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1                 # THEN move i
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded