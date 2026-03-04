from lc import *
# ===================================================================
# 1582. Special Positions in a Binary Matrix
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
# ===================================================================


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows, cols = [0] * n, [0] * m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        return sum(mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1
            for i in range(n)
            for j in range(m))


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        total = 0
        for row in range(len(mat)):
            if mat[row].count(1) == 1:
                index = mat[row].index(1)
                if [col[index] for col in mat].count(1) == 1:
                    total += 1
        return total


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = [sum(row) for row in mat]
        c = [sum(col) for col in zip(*mat)]
        return sum((r[i]==c[j]==mat[i][j]==1) for i in range(len(mat)) for j in range(len(mat[0])))


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(sum(col)==1==sum(mat[col.index(1)]) for col in zip(*mat))


test("""
Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
 
Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.


""")
