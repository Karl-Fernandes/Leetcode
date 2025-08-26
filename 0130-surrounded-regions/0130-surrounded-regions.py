class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def traverse(r, c):
            if r < 0 or c < 0 or c >= COLS or r >= ROWS or board[r][c] != 'O':
                return
            
            board[r][c] = '#'
            for dr, dc in DIRECTIONS:
                traverse(r + dr, c + dc)

        for c in range(COLS): 
            if board[0][c] == "O":
                traverse(0, c)
            if board[ROWS - 1][c] == "O":
                traverse(ROWS - 1, c)
        

        for r in range(ROWS):
            if board[r][0] == "O":
                traverse(r, 0)
            if board[r][COLS - 1] == "O":
                traverse(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

        