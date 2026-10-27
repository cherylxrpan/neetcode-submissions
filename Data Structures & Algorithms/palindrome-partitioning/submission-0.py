class Solution:
    def isPalindrome(self, s:str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        sublist = []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(sublist.copy())
                return
            if self.isPalindrome(s[j:i+1]):
                sublist.append(s[j:i+1])
                dfs(i+1, i+1)
                sublist.pop()

            dfs(j, i+1)

        dfs(0, 0)
        return res