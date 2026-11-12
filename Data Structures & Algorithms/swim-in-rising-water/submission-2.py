class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == n-1 and c == n-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))















# Idea: always expand the reachable cell that needs the lowest water level to get to. The first time you pop the exit, that level is the answer.