from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def valid_scope(coordinates):
            nonlocal grid
            if coordinates[0] < 0 or coordinates[1] < 0:
                return False
            if coordinates[0] >= len(grid) or coordinates[1] >= len(grid[0]):
                return False
            return True

        q = deque()

        # getting list of all the treasure chests
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 0:
                    q.append((i, j))

        matrix = [
            (0, 1), (1,0), (0,-1), (-1,0)
        ]

        while q:
            temp = q.popleft()
            for m in matrix:
                temp2 = (temp[0] + m[0], temp[1] + m[1])

                if not valid_scope(temp2):
                    continue

                if grid[temp2[0]][temp2[1]] == -1:
                    continue

                if grid[temp2[0]][temp2[1]] != 2147483647:
                    continue
                
                grid[temp2[0]][temp2[1]] = grid[temp[0]][temp[1]] + 1
                q.append(temp2)