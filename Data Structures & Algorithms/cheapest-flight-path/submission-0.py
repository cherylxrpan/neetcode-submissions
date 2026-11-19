class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        best_stops = [float('inf')] * n    
        heap = [(0, src, 0)]       # (cost, node, flights taken)
        while heap:
            d, u, used = heapq.heappop(heap)
            if u == dst:
                return d      
            if used >= best_stops[u] or used > k:
                continue        
            best_stops[u] = used
            for v, w in adj[u]:
                heapq.heappush(heap, (d + w, v, used + 1))
                
        return -1