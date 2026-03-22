from lc import *
# ===================================================================================
# 1886. Determine Whether Matrix Can Be Obtained By Rotation
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
# ===================================================================================


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate(mat):
            n = len(mat)

            for i in range(n//2):
                for j in range(n):
                    mat[i][j], mat[n-1-i][j] = mat[n-1-i][j], mat[i][j]

            for i in range(n):
                for j in range(i+1):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            return mat == target

        for _ in range(4):
            if rotate(mat): return True
        return False


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):
            for i in range(n//2):
                for j in range((n+1) // 2):
                    (
                        mat[i][j],
                        mat[n-1-j][i],
                        mat[n-1-i][n-1-j],
                        mat[j][n-1-i],
                    ) = (
                        mat[n-1-j][i],
                        mat[n-1-i][n-1-j],
                        mat[j][n-1-i],
                        mat[i][j],
                    )
            if mat == target:
                return True
        return False


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        return any(target==(mat:=[*map(list, zip(*mat[::-1]))]) for _ in range(4))


test("""
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
 
Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

 
Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.


""")
