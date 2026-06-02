class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_length = 0


        def dfs(i, j):

            #base case
            if grid[i][j] == 0:
                return 0
            
            total = 0
            visited.add((i, j))

            #top
            if i - 1 >= 0 and (i - 1, j) not in visited:

                total += dfs(i - 1, j)

            #right
            if i + 1 <= len(grid) - 1 and (i + 1, j) not in visited:

                total += dfs(i + 1, j)


            #left
            if j - 1 >= 0 and (i, j-1) not in visited:

                total += dfs(i, j-1)

            #bottom
            if j + 1 <= len(grid[0]) - 1 and (i, j+1) not in visited:

                total += dfs(i, j+1)
                
            
            return total + 1


        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                curr = dfs(i, j) 
                max_length = max(curr, max_length)

        
        return max_length

                
