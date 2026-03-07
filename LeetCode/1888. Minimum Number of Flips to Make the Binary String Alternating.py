from lc import *
# ============================================================================================
# 1888. Minimum Number of Flips to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
# ============================================================================================


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        total = len(s)

        st1, st2 = "", ""
        for i in range(len(s)):
            st1 += "1" if i % 2 else "0"
            st2 += "0" if i % 2 else "1"

        diff1, diff2 = 0, 0
        l = 0
        for r in range(len(s)):
            diff1 += 1 if s[r] != st1[r] else 0
            diff2 += 1 if s[r] != st2[r] else 0

            if (r - l + 1) > n:
                diff1 -= 1 if s[l] != st1[l] else 0
                diff2 -= 1 if s[l] != st2[l] else 0
                l += 1
            
            if (r - l + 1) == n:
                total = min(total, diff1, diff2)
        
        return total


class Solution:
    def minFlips(self, s: str) -> int:
        wn = len(s)
        s *= 2
        n = len(s)

        def solve(t) -> int:
            current = 0
            prev = ["0"] * n
            
            for i in range(wn):
                if s[i] != t:
                    current += 1
                prev[i] = t
                t = "1" if t == "0" else "0"

            total = current
            for i in range(wn, n):
                if s[i-wn] != prev[i - wn]:
                    current -= 1
                if s[i] != t:
                    current += 1
                total = min(total, current)
                t = "1" if t == "0" else "0"

            return total

        return min(solve("0"), solve("1"))


test("""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

 
Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

 
Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.


""")
