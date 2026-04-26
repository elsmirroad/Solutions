from lc import *
# =========================================================
# 3912. Valid Elements in an Array
# https://leetcode.com/problems/valid-elements-in-an-array/
# =========================================================


class Solution: # O(n**2)
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        total = []
        for i in range(n):
            left = max(nums[:i] if nums[:i] else [0]) 
            curr = nums[i]
            right = max(nums[i+1:] if nums[i+1:] else [0])
            if left < curr or right < curr:
                total.append(nums[i])
        return total


class Solution: # O(n)
    def findValidElements(self, nums: list[int]) -> list[int]:
        s = set([0, len(nums) - 1])
        left, right = nums[0], nums[-1]

        for i in range(1, len(nums)):
            if nums[i] > left: s.add(i)
            left = max(left, nums[i])

        for i in range(len(nums)-2, -1, -1):
            if nums[i] > right: s.add(i)
            right = max(right, nums[i])

        return [nums[i] for i in sorted(s)]


test("""
You are given an integer array nums.
An element nums[i] is considered valid if it satisfies at least one of the following conditions:

It is strictly greater than every element to its left.
It is strictly greater than every element to its right.

The first and last elements are always valid.
Return an array of all valid elements in the same order as they appear in nums.
 
Example 1:

Input: nums = [1,2,4,2,3,2]
Output: [1,2,4,3,2]
Explanation:

nums[0] and nums[5] are always valid.
nums[1] and nums[2] are strictly greater than every element to their left.
nums[4] is strictly greater than every element to its right.
Thus, the answer is [1, 2, 4, 3, 2].


Example 2:

Input: nums = [5,5,5,5]
Output: [5,5]
Explanation:

The first and last elements are always valid.
No other elements are strictly greater than all elements to their left or to their right.
Thus, the answer is [5, 5].


Example 3:

Input: nums = [1]
Output: [1]
Explanation:
Since there is only one element, it is always valid. Thus, the answer is [1].

 
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


""")
