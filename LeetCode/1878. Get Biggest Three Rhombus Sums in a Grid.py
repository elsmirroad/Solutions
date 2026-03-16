from lc import *
# =======================================================================
# 1878. Get Biggest Three Rhombus Sums in a Grid
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
# =======================================================================


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        result = set()

        for i in range(n):
            for j in range(m):
                result.add(grid[i][j])
                s = 1
                while i - s * 2 >= 0 and j - s >= 0 and j + s < m:
                    curr = (
                        grid[i][j] # bot
                        + grid[i-s*2][j] # top
                        + grid[i-s][j-s] # left
                        + grid[i-s][j+s] # right
                    )

                    for step in range(1, s):
                        curr += (
                            grid[i-step][j-step] # bot left
                            + grid[i-step][j+step] # bot right
                            + grid[i-s*2+step][j-step] # top left
                            + grid[i-s*2+step][j+step] # top right
                        )
                    result.add(curr)
                    s += 1

        return sorted(result, reverse=True)[:3]



test("""
You are given an m x n integer matrix grid.
A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:

Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.
Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.
 
Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211

Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)

Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].

 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 10^5


""")
