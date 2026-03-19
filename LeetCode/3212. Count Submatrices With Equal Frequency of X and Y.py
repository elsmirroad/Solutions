from lc import *
# ================================================================================
# 3212. Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# ================================================================================


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m, total = len(grid), len(grid[0]), 0
        x = [[0] * m for _ in range(n)]
        y = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):

                x[i][j] = (
                    (x[i-1][j] if i > 0 else 0) +
                    (x[i][j-1] if j > 0 else 0) +
                    (1 if grid[i][j] == "X" else 0) -
                    (x[i-1][j-1] if i > 0 and j > 0 else 0)
                )

                y[i][j] = (
                    (y[i-1][j] if i > 0 else 0) +
                    (y[i][j-1] if j > 0 else 0) +
                    (1 if grid[i][j] == "Y" else 0) -
                    (y[i-1][j-1] if i > 0 and j > 0 else 0)
                )

                if x[i][j] and x[i][j] == y[i][j]: total += 1

        return total


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m, total = len(grid), len(grid[0]), 0
        cX, cY = [0] * m, [0] * m

        for i in range(n):
            rX, rY = 0, 0
            for j in range(m):
                rX += 1 if grid[i][j] == "X" else 0
                rY += 1 if grid[i][j] == "Y" else 0
                cX[j], cY[j] = cX[j] + rX, cY[j] + rY
                if cX[j] and cX[j] == cY[j]: total += 1
        return total


test("""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.

 
Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]
Output: 3
Explanation:


Example 2:

Input: grid = [["X","X"],["X","Y"]]
Output: 0
Explanation:
No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]
Output: 0
Explanation:
No submatrix has at least one 'X'.

 
Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.


""")
