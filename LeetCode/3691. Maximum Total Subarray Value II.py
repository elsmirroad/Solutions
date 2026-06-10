from lc import *
# ==============================================================
# 3691. Maximum Total Subarray Value II
# https://leetcode.com/problems/maximum-total-subarray-value-ii/
# ==============================================================


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.st = [(0, 0) for _ in range(4*self.n)]
        self.build(1, 0, self.n-1)

    def build(self, node, l, r):
        if l == r: self.st[node] = (self.arr[l], self.arr[l]); return
        mid = l+(r-l) // 2
        self.build(2*node, l, mid)
        self.build(2*node+1, mid+1, r)
        self.st[node] = (
            max(self.st[node*2][0], self.st[node*2+1][0]),
            min(self.st[node*2][1], self.st[node*2+1][1])
        )

    def query(self, ql, qr, node=1, l=0, r=None):
        if r == None: r = self.n-1
        if ql > r or qr < l: return (-inf, inf)
        if ql <= l and qr >= r: return self.st[node]
        mid = l+(r-l) // 2
        lmx, lmn = self.query(ql, qr, node*2, l, mid)
        rmx, rmn = self.query(ql, qr, node*2+1, mid+1, r)
        return (
            max(lmx, rmx),
            min(lmn, rmn)
        )


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SegmentTree(nums)
        mxHeap = []

        mx, mn = st.query(0, n-1)
        heapq.heappush(mxHeap, (-(mx-mn), 0, n-1))
        seen = set()
        seen.add((0, n-1))
        total = 0

        while k:
            k -= 1
            v, l, r = heapq.heappop(mxHeap)
            v = -v
            total += v
            if l+1 <= r and not (l+1, r) in seen:
                mx, mn = st.query(l+1, r)
                heapq.heappush(mxHeap, (-(mx-mn), l+1, r))
                seen.add((l+1, r))
            if r-1 >= l and not (l, r-1) in seen:
                mx, mn = st.query(l, r-1)
                heapq.heappush(mxHeap, (-(mx-mn), l, r-1))
                seen.add((l, r-1))

        return total


test("""
You are given an integer array nums of length n and an integer k.
You must select exactly k distinct subarrays nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.
The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).
The total value is the sum of the values of all chosen subarrays.
Return the maximum possible total value you can achieve.
 
Example 1:

Input: nums = [1,3,2], k = 2
Output: 4
Explanation:
One optimal approach is:

Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.

Adding these gives 2 + 2 = 4.

Example 2:

Input: nums = [4,2,5,1], k = 3
Output: 12
Explanation:
One optimal approach is:

Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
Choose nums[1..3] = [2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.

Adding these gives 4 + 4 + 4 = 12.

 
Constraints:

1 <= n == nums.length <= 5 * 10^​​​​​​​4
0 <= nums[i] <= 10^9
1 <= k <= min(10^5, n * (n + 1) / 2)


""")
