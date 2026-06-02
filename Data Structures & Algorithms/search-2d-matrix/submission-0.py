class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix == None:
            return false

        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m*n - 1

        while start <= end:
            temp = (start + end) // 2

            if matrix[temp // n][temp % n] > target:
                end = temp - 1
            elif matrix[temp // n][temp % n] < target:
                start = temp + 1
            else:
                return True

        return False
                
