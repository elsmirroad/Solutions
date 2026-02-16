from lc import *
# ============================================================
# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# ============================================================


class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for _ in range(32):
            r <<= 1
            r |= (n % 2)
            n >>= 1
        return r


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


test("""
Reverse bits of a given 32 bits signed integer.
 
Example 1:

Input: n = 43261596
Output: 964176192
Explanation:



Integer
Binary


43261596
00000010100101000001111010011100


964176192
00111001011110000010100101000000




Example 2:

Input: n = 2147483644
Output: 1073741822
Explanation:



Integer
Binary


2147483644
01111111111111111111111111111100


1073741822
00111111111111111111111111111110




 
Constraints:

0 <= n <= 231 - 2
n is even.

 
Follow up: If this function is called many times, how would you optimize it?

""")
