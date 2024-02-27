# Valid Sudoku Constraints and Hints

## Constraints
-   `board.length == 9`
-   `board[i].length == 9`
-   `board[i][j] is a digit 1-9 or '.'`

## Hint #1
> Each row, column, and 3x3 box require unique values. How can we ensure that we have unique values for every row, every column, and every 3x3 box?

## Hint #2
> There are 9 rows, 9 columns, and 9 boxes. This means that we would need 27 sets! Is there perhaps a way we can organize these sets?

## Hint #3
> It is pretty easy to uniquely identify each row and column by index. However, uniquely identifying each box is going to require that we check whether the column and row indices fall into certain ranges.