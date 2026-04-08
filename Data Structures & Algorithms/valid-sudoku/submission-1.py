class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Brute-force Solution
        # We validate the Sudoku board by checking three main rules independently.
        # Note: Since the board is strictly 9x9, the strict Time and Space complexity is O(1).
        # If generalized for an N x N board, it would be Time: O(N^2) and Space: O(N).

        # 1. Check if each row is valid (no duplicate digits from 1-9)
        for i in board:
            digit_set = set()
            for j in i:
                if j == ".":
                    continue
                # If the digit is already in our set, the row is invalid
                if j in digit_set:
                    return False
                digit_set.add(j)
                
        # 2. Check if each column is valid
        for i in range(9):
            digit_set = set()
            for j in range(9):
                # i represents the column index, j represents the row index
                if board[j][i] == ".":
                    continue
                if board[j][i] in digit_set:
                    return False
                digit_set.add(board[j][i])
                
        # 3. Check if each 3x3 sub-box is valid
        x = 0
        for _ in range(3):
            y = 0
            for _ in range(3):
                digit_set = set() # Use set instead of list for O(1) lookup time
                # Iterate through the specific 3x3 sub-box boundaries
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in digit_set:
                            return False
                        digit_set.add(board[i][j])
                # Move to the next 3x3 box in the same row block
                y += 3
            # Move down to the next row block of 3x3 boxes
            x += 3
            
        # If all checks pass, the board is valid
        return True