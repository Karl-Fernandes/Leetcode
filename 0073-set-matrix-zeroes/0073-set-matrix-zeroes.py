class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][c] == 0 for c in range(COLS))
        first_col_zero = any(matrix[r][0] == 0 for r in range(ROWS))

        # Step 2: use first row/col as markers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 3: zero cells based on markers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 4: handle first row
        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        # Step 5: handle first col
        if first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
