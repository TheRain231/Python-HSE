"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/valid-sudoku/description
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                for x in range(9):
                    if board[i][x] == board[i][j] and x != j:
                        return False
                    if board[x][j] == board[i][j] and x != i:
                        return False
                for x in range(i // 3 * 3, i // 3 * 3 + 3):
                    for y in range(j // 3 * 3, j // 3 * 3 + 3):
                        if x == i and y == j:
                            continue
                        if board[x][y] == board[i][j]:
                            print(board[x][y])
                            return False
        return True
