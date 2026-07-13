from lc import *
# ================================================
# 1291. Sequential Digits
# https://leetcode.com/problems/sequential-digits/
# ================================================


class Solution:
    nums = [*range(1, 10)]
    for num in nums:
        d = num % 10
        if d < 9: nums.append(num * 10 + d + 1)
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [num for num in self.nums if low <= num <= high]


test("""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
 
Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

 
Constraints:

10 <= low <= high <= 10^9


""")
