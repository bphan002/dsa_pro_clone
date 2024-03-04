# Search a 2D Matrix Constraints and Hints

## Constraints
-   `m == matrix.length`
-   `n == matrix[i].length`
-   `1 <= m, n <= 100`
-   `-10^4 <= matrix[i][j], target <= 10^4`

## Hint #1
> Binary search vertically to find the correct row, then you can binary search normally in the horizontal direction.