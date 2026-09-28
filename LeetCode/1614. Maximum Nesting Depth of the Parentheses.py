from lc import *
# =======================================================================
# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# =======================================================================


class Solution:
    def maxDepth(self, s: str) -> int:
        mx = curr = 0
        for char in s:
            if char == '(': curr += 1
            elif char == ')': mx = max(mx, curr); curr -= 1
        return mx


class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate(seg.count('(') - seg.count(')') for seg in s))


test("""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
 
Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"
Output: 3

 
Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.


""")
