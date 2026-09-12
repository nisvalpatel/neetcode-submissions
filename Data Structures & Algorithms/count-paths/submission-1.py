class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        #okay so we will create a 2d array that will store the amount of ways to get to the bottom right. so we can basically just fill it out by filling this 2d array from right to left.


        rows, cols = m, n
        matrix = [[0] * cols for _ in range(rows)] 
        matrix[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                bottom = 0
                right = 0

                #checking if we can go down
                if i + 1 < m:
                    bottom = matrix[i+1][j]
                if j + 1 < n:
                    right = matrix[i][j+1]
                
                matrix[i][j] = bottom + right + matrix[i][j]
        
        return matrix[0][0]
