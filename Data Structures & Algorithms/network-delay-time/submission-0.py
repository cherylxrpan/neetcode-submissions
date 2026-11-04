class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]              # (distance so far, node)
        visit = set()                # nodes whose distance is final
        t = 0
        while heap:
            d, node = heapq.heappop(heap)  # the closest unfinished node
            if node in visit:
                continue              # an older, longer entry: skip it
            visit.add(node)           # its distance d is final
            t = d              # distances come out in increasing order
            for nei, w in graph[node]:
                if nei not in visit:
                    heapq.heappush(heap, (d + w, nei))   # a candidate route through node

        return t if len(visit) == n else -1