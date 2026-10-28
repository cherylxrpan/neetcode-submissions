class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        time = 0
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            # One pass of the while = one minute. The rot spreads to all neighbors at the same time each minute. So each minute you must process every orange that is rotten right now, before the clock tick.
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(len(grid))
                        and nc in range(len(grid[0]))
                        and grid[nr][nc] == 1):
                        # note that you found a fresh fruit (nr, nc) next to (r, c) which is rotton, so (nr, nc) becomes rotten too.
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        # Return the minimum minutes until no fresh orange remains. If that’s impossible, return -1; that is why you need fresh and reaching fresh == 0 means success
        return time if fresh == 0 else -1
