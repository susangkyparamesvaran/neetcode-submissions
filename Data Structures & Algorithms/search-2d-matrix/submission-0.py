class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top = 0
        bottom = m - 1
        while (top <= bottom):
            row = (top + bottom) // 2
            for i in range(n):
                if matrix[row][i] == target:
                    return True
            
            if matrix[row][n-1] > target:
                bottom = row - 1
            else:
                top = row + 1
            
        return False
