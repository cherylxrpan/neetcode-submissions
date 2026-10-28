class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1
            
            while q:
                (r, c) = q.popleft()
                for (dr, dc) in directions:
                    nr, nc = r+dr, c+dc
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area