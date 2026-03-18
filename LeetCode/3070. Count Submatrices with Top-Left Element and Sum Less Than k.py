from lc import *
# ==========================================================================================
# 3070. Count Submatrices with Top-Left Element and Sum Less Than k
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
# ==========================================================================================


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k: return 0
        n, m = len(grid), len(grid[0])
        total, bound = 1, m

        for j in range(1, m):
            grid[0][j] += grid[0][j-1]
            if grid[0][j] > k:
                bound = j
                break
            total += 1

        for i in range(1, n):
            grid[i][0] += grid[i-1][0]
            if grid[i][0] > k:
                break
            total += 1
            for j in range(1, bound):
                grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]
                if grid[i][j] > k:
                    bound = j
                    break
                total += 1
        return total


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        pref = [0] * m
        total = 0

        for i in range(n):
            acc = 0
            for j in range(m):
                pref[j] += grid[i][j]
                acc += pref[j]
                if acc <= k: total += 1
                else: break
        return total


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        return sum(col <= k for row in map(accumulate, zip(*map(accumulate, grid))) for col in row)




test("""
You are given a 0-indexed integer matrix grid and an integer k.
Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.
 
Example 1:


Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
Example 2:


Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

 
Constraints:

m == grid.length 
n == grid[i].length
1 <= n, m <= 1000 
0 <= grid[i][j] <= 1000
1 <= k <= 10^9


""")
