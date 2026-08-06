class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        #lets first find the row

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom:
            middle = (top + bottom) // 2

            if matrix[middle][left] > target:
                bottom = middle - 1

            elif matrix[middle][right] < target:
                top = middle + 1

            else:
                top = middle
                bottom = middle
                break

        if top != bottom:
            return False 

        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            middle = (left + right) // 2

            if matrix[top][middle] > target:
                right = middle - 1

            elif matrix[top][middle] < target:
                left = middle + 1
            else:
                return True

        
        return False