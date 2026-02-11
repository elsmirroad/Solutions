from lc import *
# ============================================================
# 3721. Longest Balanced Subarray II
# https://leetcode.com/problems/longest-balanced-subarray-ii/
# ============================================================


class SegmentTree:
    def __init__(self, n):
        self.lazy = [0] * (4 * n)
        self.mx = [0] * (4 * n)
        self.mn = [0] * (4 * n)


    def update(self, node, l, r):
        if self.lazy[node] != 0:
            self.mx[node] += self.lazy[node]
            self.mn[node] += self.lazy[node]
            if l < r:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0


    def change_range(self, node, val, changeL, changeR, l, r):
        self.update(node, l, r)

        if l > changeR or r < changeL: return
        if l >= changeL and r <= changeR:
            self.lazy[node] += val
            self.update(node, l, r)
            return

        mid = (l + r) // 2
        self.change_range(node * 2, val, changeL, changeR, l, mid)
        self.change_range(node * 2 + 1, val, changeL, changeR, mid + 1, r)
        self.mx[node] = max(self.mx[node * 2], self.mx[node * 2 + 1])
        self.mn[node] = min(self.mn[node * 2], self.mn[node * 2 + 1])


    def left_zero(self, node, l, r):
        self.update(node, l, r)

        if self.mn[node] > 0 or self.mx[node] < 0: return -1

        if l == r:  # leaf
            if self.mn[node] == 0: return l
            else: return -1

        mid = (l + r) // 2
        left = self.left_zero(node * 2, l, mid)
        if left != -1: return left
        return self.left_zero(node * 2 + 1, mid + 1, r)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        prev = {}
        st = SegmentTree(n)

        for r in range(n):
            curr = nums[r]
            val = 1 if curr % 2 == 0 else -1

            if curr in prev:
                st.change_range(1, -val, 0, prev[curr], 0, n-1)
            st.change_range(1, val, 0, r, 0, n-1)
            prev[curr] = r

            l = st.left_zero(1, 0, n - 1)
            if l != -1: total = max(total, r-l+1)

        return total


test("""
You are given an integer array nums.
A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
Return the length of the longest balanced subarray.
 
Example 1:

Input: nums = [2,5,4,3]
Output: 4
Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.


Example 2:

Input: nums = [3,2,2,5,4]
Output: 5
Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.


Example 3:

Input: nums = [1,2,3,2]
Output: 3
Explanation:

The longest balanced subarray is [2, 3, 2].
It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.


 
Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105


""")
