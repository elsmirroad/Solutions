from lc import *
# ===========================================================
# 3742. Maximum Path Score in a Grid
# https://leetcode.com/problems/maximum-path-score-in-a-grid/
# ===========================================================


class Solution:
    def maxPathScore(self, g: List[List[int]], k: int) -> int:
        n, m = len(g), len(g[0])
        dp = [[[-inf] * (k+1) for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0

        for i in range(n):
            for j in range(m):
                for c in range(k+1):
                    if dp[i][j][c] == -inf: continue
                    if i + 1 < n:
                        nv = g[i+1][j]
                        nc = 1 if nv != 0 else 0
                        if nc + c <= k:
                            dp[i+1][j][nc + c] = max(
                                dp[i+1][j][nc+c],
                                dp[i][j][c] + nv,
                            )
                    if j + 1 < m:
                        nv = g[i][j+1]
                        nc = 1 if nv != 0 else 0
                        if nc + c <= k:
                            dp[i][j+1][nc + c] = max(
                                dp[i][j+1][nc+c],
                                dp[i][j][c] + nv,
                            )
        result = max(dp[-1][-1])
        return result if result != -inf else -1


test("""
You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.
You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.
Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1.

Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.
Note: If you reach the last cell but the total cost exceeds k, the path is invalid.
 
Example 1:

Input: grid = [[0, 1],[2, 0]], k = 1
Output: 2
Explanation:
The optimal path is:



Cell
grid[i][j]
Score
Total
			Score
Cost
Total
			Cost




(0, 0)
0
0
0
0
0


(1, 0)
2
2
2
1
1


(1, 1)
0
0
2
0
1



Thus, the maximum possible score is 2.

Example 2:

Input: grid = [[0, 1],[1, 2]], k = 1
Output: -1
Explanation:
There is no path that reaches cell (1, 1) without exceeding cost k. Thus, the answer is -1.

 
Constraints:

1 <= m, n <= 200
0 <= k <= 10^3
^grid[0][0] == 0
0 <= grid[i][j] <= 2


""")
