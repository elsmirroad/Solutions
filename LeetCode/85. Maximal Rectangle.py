from lc import *
# ============================================================
# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
# ============================================================


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        height = [0] * (m + 1)
        total = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            s = [0]
            for j in range(1, m + 1):
                while s and height[s[-1]] >= height[j]:
                    h = height[s.pop()]
                    w = j - 1 - (s[-1] if s else -1)
                    total = max(total, h * w)
                s.append(j)
        return total


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        total = 0
        if not matrix or not matrix[0]:
            return total

        n, m = len(matrix), len(matrix[0])

        heights = [0] * m
        left, right = [0] * m, [m] * m

        for i in range(n):
            curr_left, curr_right = 0, m

            for j in range(m):  # Heights
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            for j in range(m):  # Left bounds
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_left)
                else:
                    left[j] = 0
                    curr_left = j + 1

            for j in range(m - 1, -1, -1):  # Right bounds
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = m
                    curr_right = j

            for j in range(m):
                total = max(total, heights[j] * (right[j] - left[j]))

        return total


test("""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
 
Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0

Example 3:

Input: matrix = [["1"]]
Output: 1

 
Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.


""")
