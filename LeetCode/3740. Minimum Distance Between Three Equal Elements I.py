from lc import *
# ==============================================================================
# 3740. Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
# ==============================================================================


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        total = min(total, abs(i-j) + abs(j-k) + abs(k-i))
        return total if total != float('inf') else -1


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = defaultdict(list[int])
        total = inf
        for i in range(len(nums)):
            d[nums[i]].append(i)
            if len(d[nums[i]]) >= 3:
                a, b, c = d[nums[i]][-3:]
                total = min(total, abs(a - b) + abs(b - c) + abs(c - a))
        return total if total != inf else -1


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = defaultdict(list[int]); t=min((d[j][-1] - d[j][-3] for i, j in enumerate(nums) if d[j].append(i) or len(d[j]) > 2), default=inf); return t < inf and t+t or -1


test("""
You are given an integer array nums.
A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
 
Example 1:

Input: nums = [1,2,1,1,3]
Output: 6
Explanation:
The minimum distance is achieved by the good tuple (0, 2, 3).
(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:

Input: nums = [1,1,2,3,2,1,2]
Output: 8
Explanation:
The minimum distance is achieved by the good tuple (2, 4, 6).
(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]
Output: -1
Explanation:
There are no good tuples. Therefore, the answer is -1.

 
Constraints:

1 <= n == nums.length <= 100
1 <= nums[i] <= n


""")
