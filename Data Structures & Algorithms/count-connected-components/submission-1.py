class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj= [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = 0
        visit = [False] * n
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res