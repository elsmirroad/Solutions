from lc import *
# ====================================================================
# 1727. Largest Submatrix With Rearrangements
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# ====================================================================


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        total = 0

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        for i in range(n):
            matrix[i].sort(reverse=True)
            for j in range(m):
                total = max(total, matrix[i][j] * (j + 1))

        return total


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        acc = [0] * m
        total = 0

        for i in range(n):
            for j in range(m):
                acc[j] = acc[j] + 1 if matrix[i][j] else 0

            s = sorted(acc, reverse=True)
            for col in range(len(s)):
                total = max(total, s[col] * (col + 1))

        return total


test("""
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
 
Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 10^5
matrix[i][j] is either 0 or 1.


""")
