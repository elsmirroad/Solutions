from lc import *
# ===============================================
# 1861. Rotating the Box
# https://leetcode.com/problems/rotating-the-box/
# ===============================================


class Solution:
    def rotateTheBox(self, g: List[List[str]]) -> List[List[str]]:
        n, m = len(g), len(g[0])
        r = [[0] * n for _ in range(m)]
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                r[i][j] = g[n-1-j][i]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if r[i][j] == '.':
                    d[j].append((i, j))
                elif r[i][j] == '*':
                    d[j].clear()
                else:
                    if d[j]:
                        ni, nj = d[j].pop(0)
                        r[ni][nj] = '#'
                        r[i][j] = '.'
                        d[j].append((i, j))
        return r


class Solution:
    def rotateTheBox(self, g: List[List[str]]) -> List[List[str]]:
        n, m = len(g), len(g[0])
        r = [['.'] * n for _ in range(m)]
        for i, row in enumerate(g):
            bot = m - 1
            for j in range(m-1, -1, -1):
                if row[j] == '#':
                    r[bot][n-1-i] = '#'
                    bot -= 1
                elif row[j] == '*':
                    r[j][n-1-i] = '*'
                    bot = j - 1
        return r


test("""
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.
 
Example 1:


Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:


Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:


Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

 
Constraints:

m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.


""")
