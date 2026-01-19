from lc import *
# ============================================================
# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# ============================================================


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        def get_sum(i, j, size):
            return (
                pref[i + size][j + size]
                - (pref[i + size][j-1] if i + size < n and j > 0 else 0)
                - (pref[i-1][j + size] if j + size < m and i > 0 else 0)
                + (pref[i-1][j-1] if i > 0 and j > 0 else 0)
            )

        n = len(mat)
        m = len(mat[0])
        total = 0

        pref = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                pref[i][j] = (
                    mat[i][j]
                    + (pref[i-1][j] if i > 0 else 0)
                    + (pref[i][j-1] if j > 0 else 0)
                    - (pref[i-1][j-1] if i > 0 and j > 0 else 0)
                )

        for i in range(n):
            for j in range(m):
                for size in range(total, min(n - i, m - j)):
                    square = get_sum(i, j, size)

                    if square <= threshold:
                        total = size + 1
                    else: break

        return total
        
        


test("""
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
 
Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105


""")
