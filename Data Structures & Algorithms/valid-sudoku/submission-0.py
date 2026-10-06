class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            contained = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in contained:
                    return False
                else:
                    contained.add(board[row][i])
        for col in range(9):
            contained = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in contained:
                    return False
                else:
                    contained.add(board[i][col])
        for grid in range(9):
            contained = set()
            for i in range(3):
                for j in range(3):
                    row = (grid//3)*3 + i
                    col = (grid%3)*3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in contained:
                        return False
                    else:
                        contained.add(board[row][col])
        return True
