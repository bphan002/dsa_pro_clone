class Solution:
    def spiralOrder(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
                
        left, right = 0, COLS-1
        top, bottom = 0, ROWS-1

        res = []

        while len(res) < ROWS*COLS:

            # left to right
            for c in range(left, right+1):
                res.append(matrix[top][c])
            top += 1

            # top to bottom
            for r in range(top, bottom+1):
                res.append(matrix[r][right])
            right -= 1

            if left > right or top > bottom:
                break

            # right to left
            for c in range(right, left-1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

            # bottom to top
            for r in range(bottom, top-1, -1):
                res.append(matrix[r][left])
            left += 1

        return res