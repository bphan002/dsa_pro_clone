from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):
        # Remove pass and write code here
        rowHash = defaultdict(set)
        colHash = defaultdict(set)
        boxHash = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                box = (row//3,col//3)
                if board[row][col] == '.':
                    continue
                else:
                    if value in rowHash[row] or value in colHash[col] or value in boxHash[box]:
                        return False
                rowHash[row].add(value)
                colHash[col].add(value)
                boxHash[box].add(value)
        
        return True