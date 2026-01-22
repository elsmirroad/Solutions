from lc import *
# ============================================================
# 3507. Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
# ============================================================


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        func = lambda arr, n: all(arr[i-1] <= arr[i] for i in range(1, n)) 
        total, n = 0, len(nums)

        while not func(nums, n):
            total += 1
            minsum, minpos = 10**9, -1
            
            for i in range(1, n):
                currsum = nums[i-1] + nums[i]
                if currsum < minsum:
                    minsum, minpos = currsum, i

            nums[minpos-1] = minsum
            for i in range(minpos, n-1):
                nums[i] = nums[i + 1]
            n -= 1

        return total
        




test("""
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.
An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
 
Example 1:

Input: nums = [5,2,3,1]
Output: 2
Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].

The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]
Output: 0
Explanation:
The array nums is already sorted.

 
Constraints:

1 <= nums.length <= 50
-1000 <= nums[i] <= 1000


""")
