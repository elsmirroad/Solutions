from lc import *
# ========================================================
# 3866. First Unique Even Element
# https://leetcode.com/problems/first-unique-even-element/
# ========================================================


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen = list()
        removed = set()
        for num in nums:
            if num % 2 == 0:
                if num in seen:
                    seen.remove(num)
                    removed.add(num)
                if num in removed:
                    continue
                seen.append(num)
        return seen[0] if seen else -1


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen = {}
        for num in nums:
            if not num % 2: seen[num] = seen.get(num, 0) + 1
        for num in nums:
            if not num % 2 and seen[num] == 1:
                return num
        return -1


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen = Counter(nums)
        for num in nums:
            if not num % 2 and seen[num] == 1:
                return num
        return -1


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        return next((n for n in nums if not n % 2 and Counter(nums)[n] == 1), -1)


test("""
You are given an integer array nums.
Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums. If no such integer exists, return -1.
An integer x is considered even if it is divisible by 2.
 
Example 1:

Input: nums = [3,4,2,5,4,6]
Output: 2
Explanation:
Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.

Example 2:

Input: nums = [4,4]
Output: -1
Explanation:
No even integer appears exactly once, so return -1.

 
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


""")
