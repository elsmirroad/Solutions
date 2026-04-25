from lc import *
# ===============================================================================
# 3464. Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/
# ===============================================================================


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        plst = []

        for x, y in points:
            if y == 0: plst.append(x)
            elif y == side: plst.append(side*2 + (side-x))
            elif x == 0: plst.append(side * 3 + (side-y))
            elif x == side: plst.append(side + y)
        plst.sort()

        def check(mn):
            for i in range(n):
                cnt, curr = 1, i
                while cnt < k:
                    jump = bisect_left(plst, plst[curr] + mn)
                    if jump == len(plst): return False
                    if plst[i] + 4 * side - plst[jump] < mn: break
                    cnt += 1
                    curr = jump
                if cnt == k: return True
            return False

        low = 1
        high = side * 2
        while low < high:
            mid = low + (high - low + 1) // 2
            if check(mid): low = mid
            else: high = mid - 1
        return low


test("""
You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.
You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.
You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.
Return the maximum possible minimum Manhattan distance between the selected k points.
The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 
Example 1:

Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4
Output: 2
Explanation:

Select all four points.

Example 2:

Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4
Output: 1
Explanation:

Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

Example 3:

Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5
Output: 1
Explanation:

Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

 
Constraints:

1 <= side <= 10^9
4 <= points.length <= min(4 * side, 15 * 10^3)
points[i] == [xi, yi]
The input is generated such that:
	
points[i] lies on the boundary of the square.
All points[i] are unique.


4 <= k <= min(25, points.length)


""")
