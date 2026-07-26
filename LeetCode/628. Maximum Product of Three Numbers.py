from lc import *
# ===============================================================
# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/
# ===============================================================


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(); return max(prod(nums[-3:]), nums[0]*nums[1]*nums[-1])


test("""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
 
Example 1:
Input: nums = [1,2,3]
Output: 6
Example 2:
Input: nums = [1,2,3,4]
Output: 24
Example 3:
Input: nums = [-1,-2,-3]
Output: -6

 
Constraints:

3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000


""")
