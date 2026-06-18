from lc import *
# =============================================================
# 1344. Angle Between Hands of a Clock
# https://leetcode.com/problems/angle-between-hands-of-a-clock/
# =============================================================


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = 6 * minutes
        h = 30 * (hour % 12) + 0.5 * minutes
        diff = abs(m - h)
        return min(diff, 360-diff)


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m, h = 6 * minutes, 30 * (hour % 12) + 0.5 * minutes
        return min(abs(m - h), 360-abs(m - h))


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        time = hour + minutes / 60
        diff = (11*time) % 12
        return min(diff, 12-diff) * 30


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(x := abs(hour*30 - minutes*5.5), 360-x)


test("""
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
Answers within 10^-5 of the actual value will be accepted as correct.
 
Example 1:


Input: hour = 12, minutes = 30
Output: 165

Example 2:


Input: hour = 3, minutes = 30
Output: 75

Example 3:


Input: hour = 3, minutes = 15
Output: 7.5

 
Constraints:

1 <= hour <= 12
0 <= minutes <= 59


""")
