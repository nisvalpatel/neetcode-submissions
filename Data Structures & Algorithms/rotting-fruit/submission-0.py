from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = set()

        # parse through grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # rotten fruit with time
                elif grid[r][c] == 1:
                    fresh.add((r, c))    # store fresh fruit locations

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_time = 0

        while q:
            r, c, time = q.popleft()
            max_time = max(max_time, time)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr, nc) in fresh:
                    fresh.remove((nr, nc))
                    q.append((nr, nc, time + 1))

        if len(fresh) == 0:
            return max_time
        else:
            return -1