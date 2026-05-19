from lc import *
# ===================================================
# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/
# ===================================================


class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        b = set(b)
        for num in a:
            if num in b: return num
        return -1

class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        i, j = 0, 0
        n, m = len(a), len(b)
        while i < n and j < m:
            if a[i] == b[j]:
                return a[i]
            elif a[i] > b[j]: j += 1
            else: i += 1
        return -1


class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        return max(min(set(a) & set(b), default=-2), -1)


class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        return max(min(set(a) & set(b), default=-2), -1)


test("""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
 
Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

 
Constraints:

1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[j] <= 10^9
Both nums1 and nums2 are sorted in non-decreasing order.


""")
