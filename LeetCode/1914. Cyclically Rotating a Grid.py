from lc import *
# =========================================================
# 1914. Cyclically Rotating a Grid
# https://leetcode.com/problems/cyclically-rotating-a-grid/
# =========================================================


class Solution:
    def rotateGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(g), len(g[0])
        t, l, b, r = 0, 0, n-1, m-1

        while t < b and l < r:
            P = 2 * (b - t + r - l)
            rot = k % P

            for _ in range(rot):
                tmp = g[t][l]

                for i in range(l, r):
                    g[t][i] = g[t][i+1]

                for i in range(t, b):
                    g[i][r] = g[i+1][r]

                for i in range(r, l, -1):
                    g[b][i] = g[b][i-1]

                for i in range(b, t, -1):
                    g[i][l] = g[i-1][l]

                g[t+1][l] = tmp

            t, l, b, r = t+1, l+1, b-1, r-1

        return g


test("""
You are given an m x n integer matrix grid, where m and n are both even integers, and an integer k.
The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:

Return the matrix after applying k cyclic rotations to it.
 
Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.

Example 2:
  

Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.

 
Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <=^ 5000
1 <= k <= 10^9

""")
