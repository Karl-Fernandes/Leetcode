class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coordinates = set()
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] ==  0:
                    coordinates.add((r, c))
        

        for row, col in coordinates:
            for c in range(COLS):
                matrix[row][c] = 0
            for r in range(ROWS):
                matrix[r][col] = 0
        


        
        