from lc import *
# =======================================================
# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/
# =======================================================


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        answer = [intervals[0]]
        for l, r in intervals[1:]:
            pL, pR = answer[-1]
            if pL <= l and pR >= r: continue
            answer.append([l, r])
        return len(answer)


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        last = (intervals[0])
        n = len(intervals)
        for i in range(1, n):
            l, r = intervals[i]
            pl, pr = last
            if l >= pl and r <= pr: n -= 1
            else: last = (intervals[i])
        return n


class Solution:
    def removeCoveredIntervals(self, v: List[List[int]], last: int = 0) -> int:
        return sum(last > (last := min(last, b)) for a, b in sorted((a, -b) for a, b in v))


test("""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
Return the number of remaining intervals.
 
Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

 
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 10^5
All the given intervals are unique.


""")
