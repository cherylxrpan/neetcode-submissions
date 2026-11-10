class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]: # while this airport still has tickets
                dst = adj[src].pop()  # use the smallest ticket (removed for good)
                dfs(dst)
            res.append(src)  # stuck here: add it (postorder)

        dfs("JFK")
        return res[::-1]  # built back to front, so reverse