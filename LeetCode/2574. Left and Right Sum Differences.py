from lc import *
# =============================================================
# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/
# =============================================================


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        for i in range(1, n):
            leftSum[i] = nums[i-1] + leftSum[i-1]
        rightSum = [0] * n
        for i in range(n-2, -1, -1):
            rightSum[i] = nums[i+1] + rightSum[i+1]
        return [abs(leftSum[i] - rightSum[i]) for i in range(n)]


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total, left = sum(nums), 0
        answer = []
        for curr in nums:
            answer.append(abs(total - left - curr))
            left += curr; total -= curr
        return answer


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = 0; return [abs(sum(nums)-total-(total := total + curr)) for curr in nums]


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[i+1:]) - sum(nums[:i])) for i in range(len(nums))]


test("""
You are given a 0-indexed integer array nums of size n.
Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
 
Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

 
Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10^5


""")
