from lc import *
# ===================================================
# 3899. Angles of a Triangle
# https://leetcode.com/problems/angles-of-a-triangle/
# ===================================================


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides
        c1 = (a >= 0) and (b >= 0) and (c >= 0)
        c2 = (a + b > c) and (a + c > b) and (b + c > a)
        if c1 and c2:
            ac = acos((b**2 + c**2 - a**2) / (2 * b * c))
            bc = acos((a**2 + c**2 - b**2) / (2 * a * c))
            cc = math.pi - ac - bc
            return sorted([degrees(ac), degrees(bc), degrees(cc)])
        else:
            return []


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides
        if (a + b <= c or b+c <= a or a+c <= b): return []

        cosA = (b**2 + c**2 - a**2) / (2*b*c)
        cosB = (a**2 + c**2 - b**2) / (2*a*c)
        cosC = (b**2 + a**2 - c**2) / (2*a*b)

        angleA = degrees(acos(cosA))
        angleB = degrees(acos(cosB))
        angleC = degrees(acos(cosC))

        return sorted([angleA, angleB, angleC])


test("""
You are given a positive integer array sides of length 3.
Determine if there exists a triangle with positive area whose three side lengths are given by the elements of sides.
If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in degrees), sorted in non-decreasing order. Otherwise, return an empty array.
Answers within 10^-5 of the actual answer will be accepted.
 
Example 1:

Input: sides = [3,4,5]
Output: [36.86990,53.13010,90.00000]
Explanation:
You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.

Example 2:

Input: sides = [2,4,2]
Output: []
Explanation:
You cannot form a triangle with positive area using side lengths 2, 4, and 2.

 
Constraints:

sides.length == 3
1 <= sides[i] <= 1000


""")
