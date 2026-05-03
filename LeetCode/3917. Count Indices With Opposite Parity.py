from lc import *
# =================================================================
# 3917. Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/
# =================================================================


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] % 2 and not nums[j] % 2:
                    arr[i] += 1
                elif not nums[i] % 2 and nums[j] % 2:
                    arr[i] += 1
        return arr


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [0] * n
        even, odd = 0, 0

        for i in range(n-1, -1, -1):
            if nums[i] % 2 == 0:
                arr[i] = odd
                even += 1
            else:
                arr[i] = even
                odd += 1
        return arr


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        arr = []
        odd, even = 0, 0
        for num in reversed(nums):
            if num % 2: odd+=1; arr.append(even)
            else: even+=1; arr.append(odd)
        return arr[::-1]


test("""
You are given an integer array nums of length n.
The score of an index i is defined as the number of indices j such that:

i < j < n, and
nums[i] and nums[j] have different parity (one is even and the other is odd).

Return an integer array answer of length n, where answer[i] is the score of index i.
 
Example 1:

Input: nums = [1,2,3,4]
Output: [2,1,1,0]
Explanation:

nums[0] = 1, which is odd. Thus, the indices j = 1 and j = 3 satisfy the conditions, so the score of index 0 is 2.
nums[1] = 2, which is even. Thus, the index j = 2 satisfies the conditions, so the score of index 1 is 1.
nums[2] = 3, which is odd. Thus, the index j = 3 satisfies the conditions, so the score of index 2 is 1.
nums[3] = 4, which is even. Thus, no index satisfies the conditions, so the score of index 3 is 0.

Thus, the answer = [2, 1, 1, 0].

Example 2:

Input: nums = [1]
Output: [0]
Explanation:
There is only one element in nums. Thus, the score of index 0 is 0.

 
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


""")
