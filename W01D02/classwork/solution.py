from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):
        # ROWS, COLS = len(board), len(board[0])
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]

                box_coord = (r//3, c//3)

                if curr_val != ".":
                    if curr_val in rows[r] or curr_val in cols[c] or curr_val in boxes[box_coord]:
                        return False
                    
                    rows[r].add(curr_val)
                    cols[c].add(curr_val)
                    boxes[box_coord].add(curr_val)

        return True