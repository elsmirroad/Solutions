from lc import *
# ============================================================
# 2975. Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
# ============================================================


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        def get_gaps(arr: List[int], bound):
            arr = sorted([1] + arr + [bound])
            g = set()
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    g.add(arr[j] - arr[i])
            return g

        hs, vs = get_gaps(hFences, m), get_gaps(vFences, n)

        comm = hs & vs

        return max(comm) ** 2 % (10**9 + 7) if comm else -1


class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        g = lambda arr, b: {j - i for j in arr + [b] for i in [1] + arr}; return max(g(h, m) & g(v, n)) ** 2 % (10**9 + 7) or -1


test("""
There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.
Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).
Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.
Since the answer may be large, return it modulo 109 + 7.
Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.
 
Example 1:


Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

Example 2:


Input: m = 6, n = 7, hFences = [2], vFences = [4]
Output: -1
Explanation: It can be proved that there is no way to create a square field by removing fences.

 
Constraints:

3 <= m, n <= 109
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences and vFences are unique.


""")
