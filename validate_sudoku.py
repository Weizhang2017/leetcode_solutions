# https://leetcode.com/problems/valid-sudoku/
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                # print(board[i][j])
                if board[i][j] != '.':
                    # print(row)
                    # print(col)
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        # print(board[i][j])
                        return False
                if board[j][i] != '.':
                    if board[j][i] not in col:
                        col.add(board[j][i])
                    else:
                        return False

        for m in range(3):
            for n in range(3):
                cell = set()
                for i in range(3):
                    for j in range(3):
                        if board[i+m*3][j+n*3] != '.':
                            if board[i+m*3][j+n*3] not in cell:
                                cell.add(board[i+m*3][j+n*3])
                            else:
                                return False
        return True

if __name__ == '__main__':
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    print(s.isValidSudoku(board))

