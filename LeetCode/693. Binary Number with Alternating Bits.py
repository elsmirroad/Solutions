from lc import *
# ============================================================
# 693. Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/
# ============================================================


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        for i in range(1, len(n)):
            if n[i-1] == n[i]:
                return False
        return True


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, c = divmod(n, 2)
        while n:
            if n % 2 == c: return False
            n, c = divmod(n, 2)
        return True


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(a != b for a, b in pairwise(bin(n)[2:]))


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return (n^n//2)+1&n<1


test("""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
 
Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 
Constraints:

1 <= n <= 231 - 1


""")
