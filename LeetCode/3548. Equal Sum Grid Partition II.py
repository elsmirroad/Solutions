from lc import *
# ==========================================================
# 3548. Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/
# ==========================================================


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        def check(matrix):
            nn, mm = len(matrix), len(matrix[0])
            curr = 0
            seen = {} # seen[value] = [coords for first, coords for last]
            for i in range(nn-1):
                for j in range(mm):
                    value = matrix[i][j]
                    curr += value
                    if value in seen: seen[value][1] = (i, j)
                    else: seen[value] = [(i, j), (i, j)]

                diff = total - (curr*2)
                if diff == 0: return True
                if -diff in seen:
                    fr, fc = seen[-diff][0]
                    lr, lc = seen[-diff][1]
                    if mm > 1 and i + 1 > 1: return True # Big grid always connected
                    if mm > 1 and i + 1 == 1 and (fc == 0 or lc == mm-1): return True # One Row
                    if mm == 1 and (fr == 0 or lr == i): return True # One Column 

        n, m = len(grid), len(grid[0])
        total = sum(grid[i][j] for j in range(m) for i in range(n))
        if check(grid) or check(grid[::-1]): return True

        ngrid = list(zip(*grid))
        if check(ngrid) or check(ngrid[::-1]): return True
        return False


test("""
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.

Return true if such a partition exists; otherwise, return false.
Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.
 
Example 1:

Input: grid = [[1,4],[2,3]]
Output: true
Explanation:


A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.


Example 2:

Input: grid = [[1,2],[3,4]]
Output: true
Explanation:


A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.


Example 3:

Input: grid = [[1,2,4],[2,3,5]]
Output: false
Explanation:


A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.


Example 4:

Input: grid = [[4,1,8],[3,2,6]]
Output: false
Explanation:
No valid cut exists, so the answer is false.

 
Constraints:

1 <= m == grid.length <= 10^5
1 <= n == grid[i].length <= 10^5
2 <= m * n <= 10^5
1 <= grid[i][j] <= 10^5


""")
