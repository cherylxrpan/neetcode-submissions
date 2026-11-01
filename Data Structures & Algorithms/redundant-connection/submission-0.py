class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]       # nodes are 1..n

        def connected(u, v, visit):            # can u reach v using edges added so far?
            if u == v:
                return True
            visit[u] = True
            for nei in adj[u]:
                if not visit[nei] and connected(nei, v, visit):
                    return True
            return False

        for u, v in edges:
            if connected(u, v, [False] * (n + 1)):   # already connected?
                return [u, v]                        # → this edge closes the cycle
            adj[u].append(v)                         # otherwise add it
            adj[v].append(u)