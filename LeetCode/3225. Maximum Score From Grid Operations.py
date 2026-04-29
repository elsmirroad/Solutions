from lc import *
# =================================================================
# 3225. Maximum Score From Grid Operations
# https://leetcode.com/problems/maximum-score-from-grid-operations/
# =================================================================


class Solution:
    def maximumScore(self, g: List[List[int]]) -> int:
        n = len(g)
        if n == 1: return 0
        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)

        for j in range(1, n):
            ndp0 = [0] * (n+1)
            ndp1 = [0] * (n+1)

            for i in range(n + 1):
                prev = 0
                curr = sum(g[x][j] for x in range(i))

                for y in range(n + 1):
                    if y > 0 and y <= i:
                        curr -= g[y-1][j]
                    if j > 0 and y > i:
                        prev += g[y-1][j-1]
                    ndp0[y] = max(ndp0[y], prev + dp0[i], dp1[i])
                    ndp1[y] = max(ndp1[y], curr + dp1[i], curr + prev + dp0[i])
            dp0, dp1 = ndp0, ndp1
        return max(dp1)


test("""
You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the j^th column starting from the top row down to the i^th row.
The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.
Return the maximum score that can be achieved after some number of operations.
 
Example 1:

Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
Output: 11
Explanation:

In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

Example 2:

Input: grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]
Output: 94
Explanation:

We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4] which is equal to 94.

 
Constraints:

1 <= n == grid.length <= 100
n == grid[i].length
0 <= grid[i][j] <= 10^9


""")
