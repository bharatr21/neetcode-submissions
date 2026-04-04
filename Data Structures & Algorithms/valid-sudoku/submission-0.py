def rowValid(board: List[List[str]], row: int) -> bool:
    seen = set()
    for col in range(9):
        if board[row][col] != '.' and board[row][col] in seen:
            return False
        seen.add(board[row][col])
    return True

def colValid(board: List[List[str]], col: int) -> bool:
    seen = set()
    for row in range(9):
        if board[row][col] != '.' and board[row][col] in seen:
            return False
        seen.add(board[row][col])
    return True

def boxValid(board: List[List[str]], row: int, col: int) -> bool:
    seen = set()
    for r in range(row * 3, row * 3 + 3):
        for c in range(col * 3, col * 3 + 3):
            if board[r][c] != '.' and board[r][c] in seen:
                return False
            seen.add(board[r][c])
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowFlag = True
        colFlag = True
        boxFlag = True
        for row in range(9):
            rowFlag = rowFlag and rowValid(board, row)
            if not rowFlag:
                return False
        for col in range(9):
            colFlag = colFlag and colValid(board, col)
            if not colFlag:
                return False
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                boxFlag = boxFlag and boxValid(board, row // 3, col // 3)
                if not boxFlag:
                    return False
        return True
