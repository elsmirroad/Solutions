from lc import *
# ================================================================================
# 1320. Minimum Distance to Type a Word Using Two Fingers
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
# ================================================================================


class Solution:
    def minimumDistance(self, word: str) -> int:

        d = {}
        for char in word:
            pos = ord(char) - ord('A')
            i, j = pos//6, pos%6
            d[char] = (i, j)

        def getDist(a, b):
            if a is None: return 0
            x, y = d[a], d[b]
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        @cache
        def getMin(idx, f1, f2):
            if idx == len(word): return 0
            char = word[idx]
            d1 = getDist(f1, char) + getMin(idx+1, char, f2)
            d2 = getDist(f2, char) + getMin(idx+1, f1, char)
            return min(d1, d2)

        return getMin(0, None, None)


class Solution:
    def minimumDistance(self, word: str) -> int:
        def dp(si, f1, f2):
            if si == len(word): return 0
            best = inf

            c = word[si]
            pos = ord(c) - ord('A')
            i, j = pos//6, pos%6

            d1 = 0 if f1 == (-1, -1) else abs(f1[0] - i) + abs(f1[1] - j)
            best = min(best, d1 + dp(si + 1, (i, j), f2))

            d2 = 0 if f2 == (-1, -1) else abs(f2[0] - i) + abs(f2[1] - j)
            best = min(best, d2 + dp(si + 1, f1, (i, j)))

            return best

        return dp(0, (-1, -1), (-1, -1))




test("""

You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).

Given the string word, return the minimum total distance to type such string using only two fingers.
The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.
 
Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3

Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6

 
Constraints:

2 <= word.length <= 300
word consists of uppercase English letters.


""")
