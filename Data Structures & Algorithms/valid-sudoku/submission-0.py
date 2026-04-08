class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            digit_list = set()
            for j in i:
                if j == ".":
                    continue
                if j in digit_list:
                    return False
                digit_list.add(j)
        for i in range(9):
            digit_list = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in digit_list:
                    return False
                digit_list.add(board[j][i])

        x = 0
        for _ in range(3):
            y = 0
            for _ in range(3):
                digit_list = set()
                for i in range(x , x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in digit_list:
                            return False
                        digit_list.add(board[i][j])
                y += 3
            x += 3
        return True