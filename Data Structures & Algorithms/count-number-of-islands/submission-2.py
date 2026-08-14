class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        def dfs(coords): 
            if coords[0] < 0 or coords[0] >= len(grid):
                return
            if coords[1] < 0 or coords[1] >= len(grid[0]):
                return
            
            if (coords[0],coords[1]) in visited:
                return
            
            visited.add(coords)

            if grid[coords[0]][coords[1]] == "0":
                return
            
            offsets = [(0,1), (0, -1), (1,0), (-1,0)]

            for offset in offsets:
                new_x = offset[0] + coords[0]
                new_y = offset[1] + coords[1]

                dfs((new_x, new_y))
            
            return
        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                if grid[i][j] == "1":
                    count += 1
                    dfs((i,j))
                visited.add((i,j))
        
        return count

            

