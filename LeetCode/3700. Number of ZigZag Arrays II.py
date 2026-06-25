from lc import *
# =========================================================
# 3700. Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/
# =========================================================


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        def matrixMult(a, b):
            n1, m1 = len(a), len(a[0])
            result = [[0] * m1 for _ in range(n1)]
            for i in range(n1):
                for j in range(m1):
                    for k in range(m1):
                        result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % (10**9+7)
            return result

        def matrixPow(base, exp, result):
            while exp:
                if exp % 2 == 1: result = matrixMult(result, base)
                base = matrixMult(base, base)
                exp //= 2
            return result

        items = r-l+1
        size = 2 * items
        matrix = [[0] * size for _ in range(size)]
        for i in range(items):

            for j in range(i): # move Down
                matrix[i][j+items] = 1

            for j in range(i+1, items): # move Up
                matrix[i+items][j] = 1

        dp = [[1] * size]
        dp = matrixPow(matrix, n-1, dp)
        return sum(dp[-1]) % (10**9+7)




test("""
You are given three integers n, l, and r.
A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.

Return the total number of valid ZigZag arrays.
Since the answer may be large, return it modulo 10^9 + 7.
A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).
 
Example 1:

Input: n = 3, l = 4, r = 5
Output: 2
Explanation:
There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]


Example 2:

Input: n = 3, l = 1, r = 3
Output: 10
Explanation:
​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]

All arrays meet the ZigZag conditions.

 
Constraints:

3 <= n <= 10^9
1 <= l < r <= 75​​​​​​​


""")
