from lc import *
# =======================================================================
# 1594. Maximum Non Negative Product in a Matrix
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
# =======================================================================


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        maxdp = [[0] * m for _ in range(n)]
        mindp = [[0] * m for _ in range(n)]
        mindp[0][0] = maxdp[0][0] = grid[0][0]

        for i in range(1, n):
            maxdp[i][0] = mindp[i][0] = maxdp[i-1][0] * grid[i][0]

        for j in range(1, m):
            maxdp[0][j] = mindp[0][j] = maxdp[0][j-1] * grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] >= 0:
                    maxdp[i][j] = max(maxdp[i][j-1], maxdp[i-1][j]) * grid[i][j]
                    mindp[i][j] = min(mindp[i][j-1], mindp[i-1][j]) * grid[i][j]
                else:
                    maxdp[i][j] = min(mindp[i][j-1], mindp[i-1][j]) * grid[i][j]
                    mindp[i][j] = max(maxdp[i][j-1], maxdp[i-1][j]) * grid[i][j]

        if maxdp[n-1][m-1] < 0: return -1
        return maxdp[n-1][m-1] % (10**9+7)


test("""
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
Return the maximum non-negative product modulo 10^9 + 7. If the maximum product is negative, return -1.
Notice that the modulo is performed after getting the maximum product.
 
Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).

Example 3:


Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).

 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4


""")
