class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        res = 0
        for node in range(n):          # try every node
            if node not in visit:      # not reached yet → a new component
                dfs(node)              # mark the whole component
                res += 1               # count it once
        return res
            