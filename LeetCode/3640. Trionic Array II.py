from lc import *
# ============================================================
# 3640. Trionic Array II
# https://leetcode.com/problems/trionic-array-ii/
# ============================================================


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        total = -10**9
        i = 0

        while i < n:

            # Shortest First Segment
            j = i + 1
            while j < n and nums[j] > nums[j-1]:
                j += 1
            p = j - 1
            if p == i:
                i += 1
                continue
            current = nums[p] + nums[p-1]

            # Full Second Segment
            while j < n and nums[j] < nums[j-1]:
                current += nums[j]
                j += 1
            q = j - 1
            if (
                p == q or
                q == n - 1 or
                (q < n - 1 and nums[q] == nums[j])
            ):
                i = q
                continue

            # Maximum Sum Segment 
            current += nums[j]
            j += 1 
            acc, mx = 0, 0
            while j < n and nums[j] > nums[j - 1]:
                acc += nums[j]
                mx = max(mx, acc)
                j += 1 
            current += mx

            # Maximize First Segment
            acc, mx = 0, 0
            jj = p - 2
            while jj >= 0 and nums[jj] < nums[jj+1]:
                acc += nums[jj]
                mx = max(mx, acc)
                jj -= 1
            current += mx

            total = max(total, current)
            i = q # Next Start

        return total



test("""
You are given an integer array nums of length n.
A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

nums[l...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...r] is strictly increasing.

Return the maximum sum of any trionic subarray in nums.
 
Example 1:

Input: nums = [0,-2,-1,-3,0,2,-1]
Output: -4
Explanation:
Pick l = 1, p = 2, q = 3, r = 5:

nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.


Example 2:

Input: nums = [1,4,2,7]
Output: 14
Explanation:
Pick l = 0, p = 1, q = 2, r = 3:

nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
Sum = 1 + 4 + 2 + 7 = 14.


 
Constraints:

4 <= n = nums.length <= 105
-109 <= nums[i] <= 109
It is guaranteed that at least one trionic subarray exists.


""")
