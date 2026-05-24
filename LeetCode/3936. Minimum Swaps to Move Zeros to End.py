from lc import *
# =================================================================
# 3936. Minimum Swaps to Move Zeros to End
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/
# =================================================================


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        i, j = 0, n-1
        total = 0
        while i < j:
            while nums[j] == 0:
                j -= 1
                if j <= 0 or j < i: return total
            if nums[i] == 0 and nums[j] != 0:
                total += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return total


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        return nums[:-nums.count(0)].count(0)


test("""
You are given an integer array nums.
In one operation, you can choose any two distinct indices i and j and swap nums[i] and nums[j].
Return an integer denoting the minimum number of operations required to move all 0s to the end of the array.
 
Example 1:

Input: nums = [0,1,0,3,12]
Output: 2
Explanation:
We perform the following swap operations:

Swap nums[0] and nums[3], giving nums = [3, 1, 0, 0, 12].
Swap nums[2] and nums[4], giving nums = [3, 1, 12, 0, 0].

Thus, the answer is 2.

Example 2:

Input: nums = [0,1,0,2]
Output: 1
Explanation:
We perform the following swap operations:

Swap nums[0] and nums[3], giving nums = [2, 1, 0, 0].

Thus, the answer is 1.

Example 3:

Input: nums = [1,2,0]
Output: 0
Explanation:
The array already satisfies the condition. Therefore, no swap operations are needed.

 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100


""")
