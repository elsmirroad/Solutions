from lc import *
# ============================================================
# 1200. Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/
# ============================================================


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = inf
        result = []

        for a, b in pairwise(arr):
            diff = b - a
            if mindiff > diff:
                mindiff = diff
                result = []
            if mindiff == diff: 
                result.append([a, b])
        
        return result


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff, n = inf, len(arr)
        result = []

        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            if mindiff > diff:
                mindiff = diff
                result = []
            if mindiff == diff: 
                result.append([arr[i-1], arr[i]])
        
        return result


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        return (mindiff := max(map(sub, s := sorted(arr), s[1:]))) and [pair for pair in pairwise(s) if sub(*pair) == mindiff]
        


test("""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

 
Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

 
Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106


""")
